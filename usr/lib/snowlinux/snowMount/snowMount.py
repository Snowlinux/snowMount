#!/usr/bin/env python

import os
import re
import sys
import subprocess
import commands

from gi.repository import Gtk, Gio

DEBUG = False
FSTAB_PATH = '/etc/fstab'

##################################################
#                  Drive Reader                  #
##################################################

def write_fstab(fstab):
    file_header = '''# /etc/fstab - generated with snowMount
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system>\t<mount point>\t<type>\t<options>\t<dump>\t<pass>'''
    lines = []
    for key in fstab:
        if fstab[key]['use_uuid']:
            new_line = 'UUID={}\t{}\t{}\t{}\t{}\t{}\n'.format(fstab[key]['fs_spec'], fstab[key]['fs_file'], fstab[key]['fs_vfstype'], fstab[key]['fs_mntops'], fstab[key]['fs_freq'], fstab[key]['fs_passno'])
        else:
            new_line = '{}\t{}\t{}\t{}\t{}\t{}\n'.format(fstab[key]['fs_spec'], fstab[key]['fs_file'], fstab[key]['fs_vfstype'], fstab[key]['fs_mntops'], fstab[key]['fs_freq'], fstab[key]['fs_passno'])
        lines.append(new_line)
    output = '{}\n{}'.format(file_header, ''.join(lines))
    try:
        with open(FSTAB_PATH, 'w') as file:
            file.write(output)
    except IOError, detail:
        return detail

def read_fstab():
    '''Returns a dict like this:
    '/dev/sda1': {'fs_file': '/',
                'fs_freq': '0',
                'fs_mntops': 'errors=remount-ro',
                'fs_passno': '1',
                'fs_spec': 'f8b392f2-4b9e-4a12-aa40-3b40817e99f3',
                'fs_vfstype': 'ext4'}
    '/dev/sda3': {'fs_file': '/home',
                'fs_freq': '0',
                'fs_mntops': 'defaults',
                'fs_passno': '2',
                'fs_spec': 'dd682fd8-81e0-4ab0-8bc6-54164af8171d',
                'fs_vfstype': 'ext4'}'''
    devices = get_devices()
    fstab = {}
    try:
        with open(FSTAB_PATH) as lines:
            for line in lines:
                if not line.startswith('#') and line.strip():
                    if line.startswith('UUID'):
                        fs_spec = line.split()[0].split('=')[1]
                        device = subprocess.check_output(['blkid', '-U', fs_spec]).strip()
                        use_uuid = True
                    elif line.startswith('LABEL'):
                        label = line.split()[0].split('=')[1]
                        device = subprocess.check_output(['blkid', '-L', label]).strip()
                        fs_spec = devices[device]['UUID']
                        use_uuid = True
                    elif line.startswith('/dev/'):
                        device = line.split()[0]
                        try:
                            fs_spec = devices[device]['UUID']
                            use_uuid = True
                        except KeyError:
                            fs_spec = line.split()[0]
                            use_uuid = False
                    else:
                        device = line.split()[0]
                        fs_spec = line.split()[0]
                        use_uuid = False

                    fs_file = line.split()[1]
                    fs_vfstype = line.split()[2]
                    fs_mntops = line.split()[3]
                    fs_freq = line.split()[4]
                    fs_passno = line.split()[5]
                    fstab[device] = {'fs_spec' : fs_spec, 'fs_file' : fs_file, 'fs_vfstype' : fs_vfstype, 'fs_mntops' : fs_mntops, 'fs_freq' : fs_freq, 'fs_passno' : fs_passno, 'use_uuid' : use_uuid}
        return fstab
    except IOError, detail:
        return detail

def get_devices():
    '''Returns a dict like this:
    '/dev/sda1': {'LABEL': '"root"',
                'TYPE': '"ext4"',
                'UUID': '"f8b392f2-4b9e-4a12-aa40-3b40817e99f3"'},
    '/dev/sda2': {'TYPE': '"swap"',
                'UUID': '"a3cebf99-3cae-4aa4-8c95-832afd565677"'}'''
    try:
        with open('/proc/partitions') as lines:
            results = (
                re.search(r'sd[a-z][0-9]+', line)
                for line in lines
            )
            device_names = ([match.group(0) for match in results if match])
        return dict(('/dev/{}'.format(device), _get_device(os.path.join('/dev/', device))) for device in device_names)
    except IOError, detail:
        return detail

def _get_device(device):
    try:
        p = subprocess.check_output(['lsblk',
                                    '-Po',
                                    'UUID,LABEL,SIZE,TYPE,FSTYPE', device])
        output = p.split()
        return dict(e.split('=') for e in output)
    except Exception, detail:
        return detail

def get_mountpoint(device, fstab):
    if device in fstab:
        return fstab[device]['fs_file']
    else:
        return ''

def update_fstab(device, mountpoint, mountoptions, fstab):
    if mountpoint == '':
        try:
            del fstab[device]
        except KeyError:
            return fstab

    if mountpoint != 'none' and not mountpoint.startswith('/'):
        raise Exception('Invalid mountpoint {}'.format(mountpoint))

    if mountpoint != 'none' and mountpoint.startswith('/'):
        if not os.path.exists(mountpoint):
            os.mkdir(mountpoint)

    if device in fstab:
        fstab[device]['fs_file'] = mountpoint
        if mountoptions != '':
            fstab[device]['fs_mntops'] = mountoptions
        else:
            fstab[device]['fs_mntops'] = 'defaults'
    else:
        devinfo = _get_device(device)
        try:
            fs_spec = devinfo['UUID'].strip('"')
            use_uuid = True
        except KeyError:
            fs_spec = device
            use_uuid = False
        fs_file = mountpoint
        fs_vfstype = devinfo['FSTYPE'].strip('"')
        fs_mntops = 'defaults'
        fs_freq = '0'
        fs_passno = '0'
        fstab[device] = {'fs_spec' : fs_spec, 'fs_file' : fs_file, 'fs_vfstype' : fs_vfstype, 'fs_mntops' : fs_mntops, 'fs_freq' : fs_freq, 'fs_passno' : fs_passno, 'use_uuid' : use_uuid}
    return fstab

def get_fstype(device, fstab):
    if device in fstab:
        return fstab[device]['fs_vfstype']
    else:
        return _get_device(device)['FSTYPE'].strip('"')

def get_size(device, devices):
    return devices[device]['SIZE'].strip('"')

def get_mountoptions(device, fstab):
    if device in fstab:
        return fstab[device]['fs_mntops']
    else:
        return 'defaults'

##################################################
#                  Main Window                   #
##################################################

class MainWindow(Gtk.Window):

    def __init__(self, devices, fstab):
        self.devices = devices
        self.fstab = fstab

        Gtk.Window.__init__(self, title='SnowMount')

        self.main_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.main_vbox)

        self.UI_INFO = """
        <ui>
          <menubar name='MenuBar'>
            <menu action='FileMenu'>
              <menuitem action='FileSave' />
              <separator />
              <menuitem action='FileQuit' />
            </menu>
            <menu action='HelpMenu'>
              <menuitem action='About' />
            </menu>
          </menubar>
        </ui>
        """

        action_group = Gtk.ActionGroup('my_actions')
        self.add_file_menu_actions(action_group)
        self.add_help_menu_actions(action_group)

        uimanager = self.create_ui_manager()
        uimanager.insert_action_group(action_group)

        menubar = uimanager.get_widget('/MenuBar')

        self.main_vbox.pack_start(menubar, False, False, 0)

        self.main_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.main_vbox.pack_start(self.main_hbox, True, True, 0)

        self.device_store = Gtk.ListStore(str)
        for device in self.devices:
            self.device_store.append([device])
        self.device_view = Gtk.TreeView(self.device_store)
        self.device_store_selection = self.device_view.get_selection()
        self.device_store_selection.connect('changed', self.on_cursor_changed)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Devices", renderer, text=0)
        self.device_view.append_column(column)
        self.main_hbox.pack_start(self.device_view, True, True, 0)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.main_hbox.pack_start(self.vbox, True, True, 0)

        self.frame = Gtk.Frame(label='sdXY')
        self.vbox.pack_start(self.frame, True, True, 6)

        self.grid = Gtk.Grid(column_spacing=5, row_spacing=5)
        self.frame.add(self.grid)
        
        self.label_size = Gtk.Label('Size: ')
        self.entry_size = Gtk.Entry()
        self.entry_size.set_editable(False)
        self.label_fstype = Gtk.Label('Filesystem: ')
        self.entry_fstype = Gtk.Entry()
        self.entry_fstype.set_editable(False)
        self.label_mountpoint = Gtk.Label('Mountpoint: ')
        self.entry_mountpoint = Gtk.Entry()
        self.entry_mountpoint.set_editable(True)
        self.label_mountoptions = Gtk.Label('Options: ')
        self.entry_mountoptions = Gtk.Entry()
        self.entry_mountoptions.set_editable(True)

        self.grid.attach(self.label_size, 0, 0, 1, 1)
        self.grid.attach(self.entry_size, 1, 0, 1, 1)
        self.grid.attach(self.label_fstype, 0, 1, 1, 1)
        self.grid.attach(self.entry_fstype, 1, 1, 1, 1)
        self.grid.attach(self.label_mountpoint, 0, 2, 1, 1)
        self.grid.attach(self.entry_mountpoint, 1, 2, 1, 1)
        self.grid.attach(self.label_mountoptions, 0, 3, 1, 1)
        self.grid.attach(self.entry_mountoptions, 1, 3, 1, 1)

        self.buttonbox = Gtk.ButtonBox()
        self.button_save = Gtk.Button('Save', Gtk.STOCK_SAVE)
        self.button_save.connect('clicked', self.on_button_save_clicked)
        self.buttonbox.add(self.button_save)

        self.vbox.pack_start(self.buttonbox, True, True, 0)

    def on_cursor_changed(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            device = model[treeiter][0]
            self.frame.set_label(device.replace('/dev/', ''))
            self.entry_size.set_text(get_size(device, self.devices))
            self.entry_fstype.set_text(get_fstype(device, self.fstab))
            self.entry_mountpoint.set_text(get_mountpoint(device, self.fstab))
            self.entry_mountoptions.set_text(get_mountoptions(device, self.fstab))
            self.current_device = device

    def on_button_save_clicked(self, widget):
        try:
            mountpoint = self.entry_mountpoint.get_text()
            mountoptions = self.entry_mountoptions.get_text()
            new_fstab = update_fstab(self.current_device, mountpoint, mountoptions, self.fstab)
            if new_fstab is not None:
                self.fstab.update(new_fstab)
                write_fstab(self.fstab)

        except Exception, detail:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
                Gtk.ButtonsType.OK, "Error!")
            dialog.format_secondary_text(detail)
            dialog.run()
            dialog.destroy()

    def add_file_menu_actions(self, action_group):
        action_filemenu = Gtk.Action("FileMenu", "File", None, None)
        action_group.add_action(action_filemenu)
        action_filesave = Gtk.Action("FileSave", None, None, Gtk.STOCK_SAVE)
        action_filesave.connect("activate", self.on_button_save_clicked)
        action_group.add_action(action_filesave)
        action_filequit = Gtk.Action("FileQuit", None, None, Gtk.STOCK_QUIT)
        action_filequit.connect("activate", self.on_menu_file_quit)
        action_group.add_action(action_filequit)

    def add_help_menu_actions(self, action_group):
        action_group.add_actions([("HelpMenu", None, "Help"), ("About", Gtk.STOCK_ABOUT, None, None, None, self.on_menu_help_about)])

    def create_ui_manager(self):
        uimanager = Gtk.UIManager()

        # Throws exception if something went wrong
        uimanager.add_ui_from_string(self.UI_INFO)

        # Add the accelerator group to the toplevel window
        accelgroup = uimanager.get_accel_group()
        self.add_accel_group(accelgroup)
        return uimanager

    def on_menu_file_quit(self, widget):
        Gtk.main_quit()

    def on_menu_help_about(self, widget):
        dialog = Gtk.AboutDialog()
        dialog.set_program_name('SnowMount')
        dialog.set_version(VERSION)
        dialog.set_license(LICENSE)
        dialog.set_copyright(COPYRIGHT)
        dialog.set_comments('A tool to manage mountpoints and options of devices.')
        dialog.run()
        dialog.destroy()

    def on_button_press_event(self, widget, event):
        # Check if right mouse button was preseed
        if event.type == Gdk.EventType.BUTTON_PRESS and event.button == 3:
            self.popup.popup(None, None, None, None, event.button, event.time)
            return True # event has been handled

if __name__ == "__main__":
    if os.getuid() != 0:
        print "Please run SnowMount as root."
        sys.exit(1)

    VERSION = commands.getoutput("/usr/lib/snowlinux/common/version.py snowmount")
    COPYRIGHT = 'Copyright (C) 2012,2013  Lars Torben Kremer <lars@snowlinux.de>, Andy Jacobsen <andy@snowlinux.de>'
    LICENSE = '''This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.'''

    if len(sys.argv) > 1:
        if "--version" in sys.argv or "-v" in sys.argv:
            print "SnowMount version " + VERSION
            sys.exit()
        if "--dry-run" in sys.argv:
            DEBUG = True
            FSTAB_PATH = '/tmp/fstab'
            if not os.path.exists(FSTAB_PATH):
                os.system('cp /etc/fstab /tmp/')
    fstab = read_fstab()
    devices = get_devices()

    win = MainWindow(devices, fstab)
    win.set_size_request(450, 250)
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
