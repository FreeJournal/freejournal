from config.config import *
import subprocess
import sys
import os
import shutil
import time

os_version = sys.platform

if 'linux' in os_version:
    #Install Bitmessage dependencies
    subprocess.call(["apt-get install openssl git python-qt4"], shell=True)

    #Install PyBitmessage from github
    try:
        subprocess.call(["git clone https://github.com/Bitmessage/PyBitmessage $HOME/PyBitmessage"], shell=True)
    except:
        print 'PyBitmessage already installed or we received a permission denied error'

    #Used to ignore the ENORMOUS amount of output generated from running PyBitmessage
    DEVNULL = open(os.devnull, 'wb')

    #Start up PyBitmessage (have to do this in order for ~/.config/PyBitmessage to be created)
    process = subprocess.Popen(["exec " + RUN_PYBITMESSAGE], shell=True, stdout=DEVNULL, stderr=DEVNULL)

    #Sleep for a second so that the above process has enough time to create ~/.config/PyBitmessage
    time.sleep(1)

    #Kill the process since we don't need it running for the rest of the installation
    process.kill()

    #Copy our modified keys.dat file to the user's ~/.config/PyBitmessage
    shutil.copyfile("./config/keys.dat", os.path.expanduser("~/.config/PyBitmessage/keys.dat"))
else:
    print 'FATAL ERROR: We detected you are using an inferior operating system to Linux...'