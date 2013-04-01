#!/usr/bin/env python

import os
import sys
import commands

from gi.repository import Gtk, Gio

import drivereader
from fstab import Fstab


DEBUG = False
FSTAB_PATH = '/etc/fstab'

##################################################
#                  Main Window                   #
##################################################

class MainWindow(Gtk.Window):
    def __init__(self):
        self.fstab = Fstab(FSTAB_PATH)
        builder = Gtk.Builder()
        builder.add_from_file('snowMount.ui')
        window = builder.get_object('main_window')
        self.disk_treeview = builder.get_object('disk_treeview')
        self.disk_label = builder.get_object('disk_label')
        self.disk_label2 = builder.get_object('disk_label2')
        
        self.part_treeview = builder.get_object('part_treeview')
        self.part_store = Gtk.ListStore(str, str, str, str)
        self.part_treeview.set_model(self.part_store)
        renderer_text = Gtk.CellRendererText()
        renderer_filesystem_text = Gtk.CellRendererText()
        renderer_filesystem_text.set_property('editable', True)
        renderer_filesystem_text.connect('edited', self.onFileSystemEdited)
        renderer_mountpoint_text = Gtk.CellRendererText()
        renderer_mountpoint_text.set_property('editable', True)
        renderer_mountpoint_text.connect('edited', self.onMountpointEdited)
        renderer_mountoptions_text = Gtk.CellRendererText()
        renderer_mountoptions_text.set_property('editable', True)
        renderer_mountoptions_text.connect('edited', self.onMountoptionsEdited)
        column = Gtk.TreeViewColumn('Partition', renderer_text, text=0)
        self.part_treeview.append_column(column)
        column = Gtk.TreeViewColumn('Filesystem', renderer_filesystem_text, text=1)
        self.part_treeview.append_column(column)
        column = Gtk.TreeViewColumn('Mountpoint', renderer_mountpoint_text, text=2)
        self.part_treeview.append_column(column)
        column = Gtk.TreeViewColumn('Options', renderer_mountoptions_text, text=3)
        self.part_treeview.append_column(column)

        self.part_filesystem = builder.get_object('part_filesystem')
        self.part_size = builder.get_object('part_size')
        self.part_label = builder.get_object('part_label')


        self.disk_store = Gtk.ListStore(str)
        self.disk_treeview.set_model(self.disk_store)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Disks", renderer, text=0)
        self.disk_treeview.append_column(column)
        self.createDiskStore()

        self.aboutdialog = builder.get_object('aboutdialog')
        self.aboutdialog.set_version(VERSION)
        self.aboutdialog.set_license(LICENSE)
        self.aboutdialog.set_copyright(COPYRIGHT)
        self.aboutdialog.set_comments('A tool to manage mountpoints and options of devices.')

        handlers = {
            'onDeleteWindow': Gtk.main_quit,
            'onButtonRefreshClicked': self.onButtonRefreshClicked,
            'onButtonSaveClicked': self.onButtonSaveClicked,
            'onButtonAboutClicked': self.onButtonAboutClicked,
            'onDiskCursorChanged': self.onDiskCursorChanged,
            'onPartCursorChanged': self.onPartCursorChanged}

        builder.connect_signals(handlers)
        window.show_all()

    def createDiskStore(self):
        disks = drivereader.get_disks()
        for disk in disks:
            self.disk_store.append(['{} ({})'.format(disks[disk].getModel(), disk)])

    def onFileSystemEdited(self, widget, path, text):
        self.part_store[path][1] = text

    def onMountpointEdited(self, widget, path, text):
        self.part_store[path][2] = text

    def onMountoptionsEdited(self, widget, path, text):
        self.part_store[path][3] = text

    def updateFstab(self, path):
        device_path = path[0]
        filesystem = path[1]
        mountpoint = path[2]
        mountoptions = path[3]
        self.fstab.updateFstab(device_path, mountpoint, mountoptions, filesystem)

    def onButtonSaveClicked(self, button):
        model, path = self.current_part[0], self.current_part[1]
        self.updateFstab(model[path])
        self.fstab.writeFstab()

    def onButtonRefreshClicked(self, button):
        self.disk_store.clear()
        self.part_store.clear()
        self.part_filesystem.set_text('')
        self.part_size.set_text('')
        self.part_label.set_text('')
        self.createDiskStore()

    def onButtonAboutClicked(self, button):
        self.aboutdialog.run()
        self.aboutdialog.hide()

    def onDiskCursorChanged(self, selection):
        self.part_store.clear()
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            device_path = model[treeiter][0].split()[-1][1:-1]
            disk = drivereader.get_disk(device_path)
            self.disk_label.set_text('{} ({})'.format(disk.getModel(), disk.getSize()))
            self.disk_label2.set_text(device_path)
            for part in disk.getPartitions():
                self.part_store.append([part, self.fstab.getFilesystem(part), self.fstab.getMountpoint(part), self.fstab.getMountoptions(part)])

    def onPartCursorChanged(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            device_path = model[treeiter][0]
            part = drivereader.get_partition(device_path)
            self.part_filesystem.set_text(part.getFilesystem())
            self.part_size.set_text(part.getSize())
            self.part_label.set_text(part.getLabel())
            self.current_part = (model, treeiter)


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

    MainWindow()
    Gtk.main()
