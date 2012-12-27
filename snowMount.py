#!/usr/bin/env python

import dircache
import io
import os
import re
import sys
import subprocess

from gi.repository import Gtk, Gio

VERSION = "1.0.1"
DEBUG = False
FSTAB_PATH = '/etc/fstab'

##################################################
#                  Drive Reader                  #
##################################################

def write_mount_point(drive, mount_point):
    new_line = ""
    # Create directory if it doesn't exist
    if not os.path.exists(mount_point) and mount_point:
        try:
            os.makedirs(mount_point)
            print "Creating directory " + mount_point
        except Exception, detail:
            print "Mount point " + mount_point + " does not exist and cannot be created: " + detail
            return

    if mount_point:
        new_line = "UUID=" + _get_UUID(drive) + " " + mount_point + " auto defaults 0 0\n"
        print "Writing line to " + FSTAB_PATH + ":\n" + new_line
    try:
        written = False
        f = io.open(FSTAB_PATH, 'r')
        lines = f.readlines()
        f.close()

        for line in lines:
            if line.find(drive) == 0:
                lines.remove(line)
        lines.append(unicode(new_line))

        f = io.open(FSTAB_PATH, 'w')

        f.writelines(lines)
        f.flush()
        f.close()
    except Exception, details:
        print details



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
                if not line.startswith('#'):
                    if line.startswith('UUID'):
                        fs_spec = line.split()[0].split('=')[1]
                        device = subprocess.check_output(['blkid', '-U', fs_spec]).strip()
                    elif line.startswith('LABEL'):
                        label = line.split()[0].split('=')[1]
                        device = subprocess.check_output(['blkid', '-L', label]).strip()
                        fs_spec = devices[device]['UUID']
                    elif line.startswith('/dev/'):
                        device = line.split()[0]
                        try:
                            fs_spec = devices[device]['UUID']
                        except KeyError:
                            fs_spec = line.split()[0]    
                    else:
                        device = line.split()[0]
                        fs_spec = line.split()[0]
                    if device is not None:
                        fs_file = line.split()[1]
                        fs_vfstype = line.split()[2]
                        fs_mntops = line.split()[3]
                        fs_freq = line.split()[4]
                        fs_passno = line.split()[5]
                        fstab[device] = {'fs_spec' : fs_spec, 'fs_file' : fs_file, 'fs_vfstype' : fs_vfstype, 'fs_mntops' : fs_mntops, 'fs_freq' : fs_freq, 'fs_passno' : fs_passno}
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
        return dict(('/dev/{}'.format(device), _get_device(device)) for device in device_names)
    except IOError, detail:
        return detail

def _get_device(device):
    device = os.path.join('/dev/', device)
    try:
        p = subprocess.check_output(['lsblk',
                                    '-Po',
                                    'UUID,LABEL,SIZE,TYPE,FSTYPE', device])
        output = p.split()
        return dict(e.split('=') for e in output)
    except Exception, detail:
        return detail


##################################################
#                  Main Window                   #
##################################################

class MainWindow:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("snowMount.ui")

        self.window = self.builder.get_object("window_main")
        self.button_cancel = self.builder.get_object("button_cancel")
        self.button_ok = self.builder.get_object("button_ok")
        self.list_store_drives = self.builder.get_object("list_store_drives")
        self.cell_renderer_mount_point = self.builder.get_object("cell_renderer_mount_point")

        read_fstab()
        self.drive_list = get_drive_list()
        self.drive_list_orig = []
        for item in self.drive_list:
            self.drive_list_orig.append(item[:])
        for drive in self.drive_list:
            titer = self.list_store_drives.append(drive)

        self.button_cancel.connect("button-release-event", Gtk.main_quit)
        self.button_ok.connect("button-release-event", self.on_button_ok_released)
        self.cell_renderer_mount_point.connect("edited", self.on_mount_point_edited)
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()

    def on_button_ok_released(self, widget, event):
        for i in range(len(self.drive_list)):
            if self.drive_list[i][2] != self.drive_list_orig[i][2]:
                write_mount_point(self.drive_list[i][0], self.drive_list[i][2])
        Gtk.main_quit()

    def on_mount_point_edited(self, renderer, path, new_text):
        self.drive_list[int(path)][2] = new_text

        titer = self.list_store_drives.get_iter(path)
        self.list_store_drives.set_value(titer, 2, new_text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if "--dry-run" in sys.argv:
            DEBUG = "--dry-run" in sys.argv
            FSTAB_PATH = '/tmp/fstab'
        if "--version" in sys.argv or "-v" in sys.argv:
            print "SnowMount version " + VERSION
            sys.exit(1)
    if os.getuid() != 0 and not DEBUG:
        print "Please run SnowMount as root."
        sys.exit(1)

    MainWindow()
    Gtk.main()
