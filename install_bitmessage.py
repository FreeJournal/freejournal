import platform
from bitmessage.install import apt_install, windows_install

if __name__ == '__main__':
    os_version = platform.dist()[0]
    if 'Ubuntu' in os_version:
        apt_install()
        print 'Installation Completed'
    elif 'windows' in os_version:
        windows_install()
    else:
        apt_install()
        print 'Installation Completed'
