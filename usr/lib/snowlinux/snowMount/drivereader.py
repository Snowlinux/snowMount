# -*- coding: utf-8 -*-

import parted
import subprocess

class DriveReader(object):
    def __init__(self):
        self.disks = Disks()._getDisks()

    def getModel(self, device_path):
        if device_path[-1].isdigit():
            return self.disks[device_path[:-1]]['model']
        else:
            return self.disks[device_path]['model']

    def getSize(self, device_path):
        if device_path[-1].isdigit():
            return self.disks[device_path[:-1]]['parts'][device_path]['size']
        else:
            return self.disks[device_path]['size']

    def getFilesystem(self, device_path):
        return self.disks[device_path[:-1]]['parts'][device_path]['filesystem']

    def getUUID(self, device_path):
        return self.disks[device_path[:-1]]['parts'][device_path]['uuid']

    def getLabel(self, device_path):
        return self.disks[device_path[:-1]]['parts'][device_path]['label']

    def getDevice(self, label=None, uuid=None):
        if label:
            dev = subprocess.check_output('blkid -L {}'.format(label).strip(), shell=True)
            return dev.strip()
        elif uuid:
            dev = subprocess.check_output('blkid -U {}'.format(uuid).strip(), shell=True)
            return dev.strip()
        else:
            return None

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

    def _getDisks(self):
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
                                                'filesystem': part.filesystem,
                                                'uuid': part.uuid,
                                                'label': part.label}

class Partition(object):
    def __init__(self, partition):
        self._partition = partition
        self.size = self._partition.getLength(unit='B')
        self.device_name = self._partition.getDeviceNodeName()
        self.device_path = self._partition.path
        self.filesystem = self._partition.fileSystem.type
        p = subprocess.check_output(['lsblk', '-Po', 'UUID', self.device_path])
        self.uuid = p.split('=')[1].strip().strip('"')
        p = subprocess.check_output(['lsblk', '-Po', 'LABEL', self.device_path])
        self.label = p.split('=')[1].strip().strip('"')


if __name__ == '__main__':
    dr = DriveReader()
    for disk in dr.disks:
        print 'Disk: {}, Model: {} Size: {}'.format(disk, dr.getModel(disk), dr.getSize(disk))
        # print 'Device\tLabel\tSize\tFilesystem\tUUID'
        for part in dr.disks[disk]['parts']:
            print '-{}\t{}\t{}\t{}\t{}'.format(part, dr.getLabel(part), dr.getSize(part), dr.getFilesystem(part), dr.getUUID(part).strip('"'))

