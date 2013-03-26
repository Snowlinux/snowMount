#!/usr/bin/env python

import os
import re
import sys
import subprocess
import commands

from gi.repository import Gtk, Gio

from drivereader import DriveReader
from fstab import Fstab


DEBUG = False
FSTAB_PATH = '/etc/fstab'

##################################################
#                  Main Window                   #
##################################################

class MainWindow(Gtk.Window):
    def __init__(self):
        self.dr = DriveReader()
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
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn('Partition', renderer, text=0)
        self.part_treeview.append_column(column)
        column = Gtk.TreeViewColumn('Filesystem', renderer, text=1)
        self.part_treeview.append_column(column)
        column = Gtk.TreeViewColumn('Mountpoint', renderer, text=2)
        self.part_treeview.append_column(column)
        column = Gtk.TreeViewColumn('Options', renderer, text=3)
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

        handlers = {
            'onDeleteWindow': Gtk.main_quit,
            'onButtonPressed': self.onButtonPressed,
            'onDiskCursorChanged': self.onDiskCursorChanged,
            'onPartCursorChanged': self.onPartCursorChanged
        }

        builder.connect_signals(handlers)
        window.show_all()

    def createDiskStore(self):
        self.disk_store.clear()
        for disk in self.dr.getDisks():
            self.disk_store.append(['{} ({})'.format(self.dr.getModel(disk), disk)])

    def onButtonPressed(self, button):
        self.createDiskStore()

    def onDiskCursorChanged(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            disk = model[treeiter][0].split()[-1][1:-1]
            self.disk_label.set_text('{} ({})'.format(self.dr.getModel(disk), self.dr.getSize(disk)))
            self.disk_label2.set_text(disk)
            self.current_disk = disk
            for part in self.dr.getParts(self.current_disk):
                self.part_store.append([part, self.fstab.getFilesystem(part), self.fstab.getMountpoint(part), self.fstab.getMountoptions(part)])

    def onPartCursorChanged(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            part = model[treeiter][0]
            self.part_filesystem.set_text(self.dr.getFilesystem(part))
            self.part_size.set_text(self.dr.getSize(part))
            self.part_label.set_text(self.dr.getLabel(part))


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
