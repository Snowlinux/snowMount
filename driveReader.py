#!/usr/bin/env python

import re
import dircache

fstab = {}

def read_fstab():
    fstab.clear()
    lines = open('/etc/fstab', 'r').readlines()
    for line in lines:
        if not line.strip(): # Ignore empty lines
            continue;
        if "#" in line: # Ignore comments
            continue;
        if "/dev/" not in line: # Ignore non-local drives for the time being
            continue;
        drives = line.strip().split(" ")
        for item in drives:
            if not item:
                drives.remove(item)
        fstab[drives[0]] = drives[1]
    return fstab

def _get_mount_point(drive_path):
    try:
        return fstab[drive_path]
    except Exception, details: # If it is not found in fstab
        return ""

def _get_drive_paths():
    paths = dircache.listdir("/dev")
    needed_paths = [];
    for path in paths:
        if re.match("sd\w\d", path):
            needed_paths.append("%s%s" % ("/dev/", path))
        if re.match("hd\w\d", path):
            needed_paths.append("%s%s" % ("/dev/", path))
    return needed_paths

def get_drive_list():
    paths = _get_drive_paths()
    content = []
    for path in paths:
        content.append([path, path, _get_mount_point(path)]) # To be implemented: Read drive name
    return content

def write_mount_point(drive, mount_point):
    print drive # Writes to fstab - To be implemented
