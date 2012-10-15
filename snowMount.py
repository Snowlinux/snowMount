#!/usr/bin/env python

import dircache
import io
import os
import re
import sys

from gi.repository import Gtk, Gio

VERSION = 0.1
DEBUG = False
fstab = {}
FSTAB_PATH = '/etc/fstab'

##################################################
#                  Drive Reader                  #
##################################################

def get_drive_list():
    paths = _get_drive_paths()
    content = []
    for path in paths:
        content.append([path, path, _get_mount_point(path)]) # To be implemented: Read drive name
    return content

def read_fstab():
    fstab.clear()
    try:
        f = io.open(FSTAB_PATH, 'r')
        for line in f:
            if not line.strip(): # Ignore empty lines
                continue
            if "#" in line: # Ignore comments
                continue
            if "/dev/" not in line: # Ignore non-local drives for the time being
                continue
            while "  " in line:
                line = line.replace("  ", " ")
            drives = line.split(" ")
            fstab[drives[0]] = drives[1]
        f.close()
    except Exception, detail:
        print detail
    return fstab

def write_mount_point(drive, mount_point):
    new_line = ""
    if mount_point:
        new_line = drive + " " + mount_point + " auto defaults 0 0\n"
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

def _get_mount_point(drive_path):
    try:
        return fstab[drive_path]
    except Exception, details: # If it is not found in fstab
        return ""

def _get_drive_paths():
    paths = dircache.listdir("/dev")
    needed_paths = []
    for path in paths:
        if re.match("sd\w\d", path):
            needed_paths.append("%s%s" % ("/dev/", path))
        if re.match("hd\w\d", path):
            needed_paths.append("%s%s" % ("/dev/", path))
    return needed_paths

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
            print "SnowMount version " + str(VERSION)
            sys.exit(1)
    if os.getuid() != 0 and not DEBUG:
        print "Please run SnowMount as root."
        sys.exit(1)

    MainWindow()
    Gtk.main()
