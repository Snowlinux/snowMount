# -*- coding: utf-8 -*-

import parted
import subprocess


def _get_devices():
    import re
    with open('/proc/partitions') as lines:
        results = (
            re.search(r'sd[a-z]', line)
            for line in lines
        )
        devices = (['/dev/{}'.format(match.group(0)) for match in results if match])
    for device in set(devices):
        yield Disk(parted.Device(device))

def get_partition(device_path):
    device = parted.Device(device_path[:-1])
    disk = Disk(device)
    return disk.getPartitions()[device_path]

def get_disk(device_path):
    device = parted.Device(device_path)
    return Disk(device)

def get_disks():
    disks = {}
    for disk in _get_devices():
        disks[disk._device_path] = disk
    return disks

def get_device_path(uuid=None, label=None):
    if label:
        dev = subprocess.check_output('blkid -L {}'.format(label).strip(), shell=True)
        return dev.strip()
    elif uuid:
        dev = subprocess.check_output('blkid -U {}'.format(uuid).strip(), shell=True)
        return dev.strip()
    else:
        return None

class Disk(object):
    def __init__(self, disk):
        self._disk = parted.Disk(disk)
        self._device_path = self._disk.device.path
        self._size = self._disk.device.getLength(unit='B')

    def getModel(self):
        return self._disk.device.model

    def getSize(self):
        for x in ['bytes','KB','MB','GB']:
            if self._size < 1024.0:
                return "%3.1f%s" % (self._size, x)
            self._size /= 1024.0
        return "%3.1f%s" % (self._size, 'TB')

    def getPartitions(self):
        partitions = {}
        for part in self._disk.partitions:
            part = Partition(part)
            partitions[part._device_path] = part
        return partitions

class Partition(object):
    def __init__(self, partition):
        self._partition = partition
        self._size = self._partition.getLength(unit='B')
        self._device_path = self._partition.path

    def getFilesystem(self):
        return self._partition.fileSystem.type

    def getUUID(self):
        p = subprocess.check_output(['lsblk', '-Po', 'UUID', self._device_path])
        return p.split('=')[1].strip().strip('"')

    def getLabel(self):
        p = subprocess.check_output(['lsblk', '-Po', 'LABEL', self._device_path])
        return p.split('=')[1].strip().strip('"')

    def getSize(self):
        for x in ['bytes','KB','MB','GB']:
            if self._size < 1024.0:
                return "%3.1f%s" % (self._size, x)
            self._size /= 1024.0
        return "%3.1f%s" % (self._size, 'TB')

    def getMountpoint(self):
        if self.isBusy():
            p = subprocess.check_output(['lsblk', '-Po', 'MOUNTPOINT', self._device_path])
            return p.split('=')[1].strip().strip('"')
        else:
            return None

    def isBusy(self):
        return self._partition.busy

if __name__ == '__main__':
    # print get_device_path('f8b392f2-4b9e-4a12-aa40-3b40817e99f3')
    part = get_partition('/dev/sdc1')
    print part.getUUID()
    disks = get_disks()
    for disk in disks:
        print 'Disk: {} ({})'.format(disks[disk].getModel(), disk)
        print 'Size: {}'.format(disks[disk].getSize())
        print 'Partitions:'
        partitions = disks[disk].getPartitions()
        for partition in partitions:
            print ' --> {} {} {} {} {} {}'.format(partition,
                                        partitions[partition].getMountpoint(),
                                        partitions[partition].getFilesystem(),
                                        partitions[partition].getSize(),
                                        partitions[partition].getLabel(),
                                        partitions[partition].getUUID())
        print '\n'
