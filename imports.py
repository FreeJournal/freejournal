import os, sys

from config import *

Bitmessage = getattr(__import__('bitmessage.bitmessage', fromlist=['']), 'Bitmessage')

Collection = getattr(__import__('backend.datastructures.collection', fromlist=['']), 'Collection')
FJMessage = getattr(__import__('backend.datastructures.fj_message', fromlist=['']), 'FJMessage')

CollectionHandler = getattr(__import__('backend.collection_handler', fromlist=['']), 'CollectionHandler')
