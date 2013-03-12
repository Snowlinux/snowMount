# -*- coding: utf-8 -*-

import parted

class Disks(object):
    '''
    '/dev/sda': {'model': 'ATA ST94813AS', 
                'parts': {'/dev/sda1': {'filesystem': 'ext4', 'size': 14998831104.0},
                          '/dev/sda2': {'filesystem': 'linux-swap(v1)', 'size': 1999634432.0},
                          '/dev/sda3': {'filesystem': 'ext4', 'size': 23007854592.0}},
                'size': 40007761920.0}}
    '''
    def __init__(self):
        self._devices = parted.getAllDevices()
        self._disks = {}
        for disk in self._devices:
            disk = Disk(disk)
            self._disks[disk.device_path] = {'model': disk.model,
                                            'size': disk.size,
                                            'parts': disk.partitions}

    def getDisks(self):
        return self._disks

class Disk(object):
    def __init__(self, disk):
        self._disk = parted.Disk(disk)
        self.device_path = self._disk.device.path
        self.model = self._disk.device.model
        self.size = self._disk.device.getLength(unit='B')
        self.partitions = {}
        for part in self._disk.partitions:
            part = Partition(part)
            self.partitions[part.device_path] = {'size': part.size,
                                                'filesystem': part.filesystem}

class Partition(object):
    def __init__(self, partition):
        self._partition = partition
        self.size = self._partition.getLength(unit='B')
        self.device_name = self._partition.getDeviceNodeName()
        self.device_path = self._partition.path
        self.filesystem = self._partition.fileSystem.type
        