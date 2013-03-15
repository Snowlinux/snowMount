# -*- coding: utf-8 -*-

import os

from drivereader import DriveReader

class Fstab(object):
    '''
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
                'fs_vfstype': 'ext4'}
    '''
    def __init__(self, filename='/etc/fstab'):
        self._filename = filename
        self._dr = DriveReader()
        self._fstab = {}
        with open(filename) as lines:
            for line in lines:
                if not line.startswith('#') and line.strip():
                    if line.startswith('UUID'):
                        fs_spec = line.split()[0].split('=')[1]
                        device = self._dr.getDevice(uuid=fs_spec)
                        use_uuid = True
                    elif line.startswith('LABEL'):
                        label = line.split()[0].split('=')[1]
                        device = self._dr.getDevice(label=label)
                        fs_spec = self._dr.getUUID(device)
                        use_uuid = True
                    elif line.startswith('/dev/'):
                        device = line.split()[0]
                        try:
                            fs_spec = self._dr.getUUID(device)
                            use_uuid = True
                        except KeyError:
                            fs_spec = line.split()[0]
                            use_uuid = False
                    else:
                        device = line.split()[0]
                        fs_spec = line.split()[0]
                        use_uuid = False
                    fs_file = line.split()[1]
                    fs_vfstype = line.split()[2]
                    fs_mntops = line.split()[3]
                    fs_freq = line.split()[4]
                    fs_passno = line.split()[5]
                    self._fstab[device] = {'fs_spec' : fs_spec, 'fs_file' : fs_file, 'fs_vfstype' : fs_vfstype, 'fs_mntops' : fs_mntops, 'fs_freq' : fs_freq, 'fs_passno' : fs_passno, 'use_uuid' : use_uuid}

    def getFstab(self):
        return self._fstab

    def getMountpoint(self, device):
        if device in self._fstab:
            return self._fstab[device]['fs_file']
        else:
            return ''

    def getMountoptions(self, device):
        if device in self._fstab:
            return self._fstab[device]['fs_mntops']
        else:
            return 'defaults'

    def getFilesystem(self, device):
        if device in self._fstab:
            return self._fstab[device]['fs_vfstype']
        else:
            return None

    def updateFstab(self, device, mountpoint, mountoptions):
        if mountpoint == '':
            del self._fstab[device]

        if mountpoint != 'none' and not mountpoint.startswith('/'):
            raise Exception('Invalid mountpoint {}'.format(mountpoint))

        if mountpoint != 'none' and mountpoint.startswith('/'):
            if not os.path.exists(mountpoint):
                os.mkdir(mountpoint)

        if device in self._fstab:
            self._fstab[device]['fs_file'] = mountpoint
            if mountoptions != '':
                self._fstab[device]['fs_mntops'] = mountoptions
            else:
                self._fstab[device]['fs_mntops'] = 'defaults'
        else:
            try:
                fs_spec = self._dr.getUUID(device)
                use_uuid = True
            except KeyError:
                fs_spec = device
                use_uuid = False
            fs_file = mountpoint
            fs_vfstype = self._dr.getFilesystem(device)
            fs_mntops = 'defaults'
            fs_freq = '0'

            ### TODO ###
            if mountpoint == '/':
                fs_passno = '1'
            elif fs_vfstype in ['ext3', 'ext4']:
                fs_passno = '2'
            else:
                fs_passno = '0'
            self._fstab[device] = {'fs_spec' : fs_spec, 'fs_file' : fs_file, 'fs_vfstype' : fs_vfstype, 'fs_mntops' : fs_mntops, 'fs_freq' : fs_freq, 'fs_passno' : fs_passno, 'use_uuid' : use_uuid}

    def writeFstab(self):
        file_header = '''# /etc/fstab - generated with snowMount
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system>\t<mount point>\t<type>\t<options>\t<dump>\t<pass>'''
        lines = []
        for key in self._fstab:
            if self._fstab[key]['use_uuid']:
                new_line = 'UUID={}\t{}\t{}\t{}\t{}\t{}\n'.format(self._fstab[key]['fs_spec'], self._fstab[key]['fs_file'], self._fstab[key]['fs_vfstype'], self._fstab[key]['fs_mntops'], self._fstab[key]['fs_freq'], self._fstab[key]['fs_passno'])
            else:
                new_line = '{}\t{}\t{}\t{}\t{}\t{}\n'.format(self._fstab[key]['fs_spec'], self._fstab[key]['fs_file'], self._fstab[key]['fs_vfstype'], self._fstab[key]['fs_mntops'], self._fstab[key]['fs_freq'], self._fstab[key]['fs_passno'])
            lines.append(new_line)
        output = '{}\n{}'.format(file_header, ''.join(lines))
        with open(self._filename, 'w') as file:
            file.write(output)


if __name__ == '__main__':
    if not os.path.exists('/tmp/fstab'):
        os.system('cp -v /etc/fstab /tmp/')
    fstab = Fstab('/tmp/fstab')
    print fstab.getFilesystem('/dev/sdb1')
    # fstab.updateFstab('/dev/sdb1', '/tmp/tmpmnt', '')
    # for key in fstab.getFstab():
        # print repr(key)
    # fstab.writeFstab()
