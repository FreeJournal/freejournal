import sys

from Freenet.install import linux_install

if __name__ == '__main__':
    os = sys.platform
    if 'linux' not in os:
        raise Exception("Invalid Operating System. lrn2penguin")
    else:
        linux_install()
