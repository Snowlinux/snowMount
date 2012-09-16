#!/usr/bin/env python

from gi.repository import Gtk, Gio

class MainWindow:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("snowMount.ui");

        self.window = self.builder.get_object("window_main")
        self.close_button = self.builder.get_object("button_cancel")

        self.close_button.connect("released", Gtk.main_quit)
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()

if __name__ == "__main__":
    MainWindow()
    Gtk.main()
