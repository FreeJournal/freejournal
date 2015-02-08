import xmlrpclib
import time
import subprocess
import os
import sys
from config.config import *

os_version = sys.platform
print 'Running BitMessage Tutorial on ' + os_version

if 'linux' in os_version:
    #Used to ignore the ENORMOUS amount of output generated from running PyBitmessage
    DEVNULL = open(os.devnull, 'wb')

    #Start up PyBitmessage
    process = subprocess.Popen([RUN_PYBITMESSAGE], shell=True, stdout=DEVNULL, stderr=DEVNULL)

    #Wait for PyBitmessage to start up before connecting via the api
    time.sleep(1)

    #Connect to PyBitmessage via xmlrpclib
    api = xmlrpclib.ServerProxy(BITMESSAGE_SERVER)

    #Test calling an api method
    print api.add(2,3)
    print api.helloWorld("Hello", "World")