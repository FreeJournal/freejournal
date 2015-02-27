import os, sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), './bitmessage/'))
print 'imports path: ' + path
sys.path.insert(1, path)

from bitmessage.bitmessage import *

path = os.path.abspath(os.path.join(os.path.dirname(__file__), './backend/datastructures/'))
print 'imports path: ' + path
sys.path.insert(1, path)

from backend.datastructures.collection import *
from backend.datastructures.fj_message import *

path = os.path.abspath(os.path.join(os.path.dirname(__file__), './backend/'))
print 'imports path: ' + path
sys.path.insert(1, path)

from backend.collection_handler import *

path = os.path.abspath(os.path.join(os.path.dirname(__file__), './bitmessage/config/'))
print 'imports path: ' + path
sys.path.insert(1, path)

from bitmessage.config.config import *

