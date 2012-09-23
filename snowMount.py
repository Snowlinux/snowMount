#!/usr/bin/env python

import driveReader
from gi.repository import Gtk, Gio

class MainWindow:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("snowMount.ui");

        self.window = self.builder.get_object("window_main")
        self.button_cancel = self.builder.get_object("button_cancel")
        self.button_ok = self.builder.get_object("button_ok")
        self.list_store_drives = self.builder.get_object("list_store_drives")
        self.cell_renderer_mount_point = self.builder.get_object("cell_renderer_mount_point")

        driveReader.read_fstab()
        self.drive_list = driveReader.get_drive_list();
        for drive in self.drive_list:
            titer = self.list_store_drives.append(drive);

        self.button_cancel.connect("button-release-event", Gtk.main_quit)
        self.button_ok.connect("button-release-event", self.on_button_ok_released)
        self.cell_renderer_mount_point.connect("edited", self.on_mount_point_edited)
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()

    def on_button_ok_released(self, widget, event):
        for drive in self.drive_list:
            driveReader.write_drive_name(drive[0], drive[2]);
        Gtk.main_quit()

    def on_mount_point_edited(self, renderer, path, new_text):
        # Update list store and self.drive_list - To be implemented
        print new_text

if __name__ == "__main__":
    MainWindow()
    Gtk.main()
