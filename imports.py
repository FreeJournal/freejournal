import os
import sys

from config import *
from cache.cache import *


path = os.path.abspath(os.path.join(os.path.dirname('~/PyBitmessage/src/')))
sys.path.insert(0, path)
import addresses

Bitmessage = getattr(__import__('bitmessage.bitmessage', fromlist=['']), 'Bitmessage')
Collection = getattr(__import__('models.collection', fromlist=['']), 'Collection')
FJMessage = getattr(__import__('backend.datastructures.fj_message', fromlist=['']), 'FJMessage')
Document = getattr(__import__('models.document', fromlist=['']), 'Document')
Keyword = getattr(__import__('models.keyword', fromlist=['']), 'Keyword')
CollectionHandler = getattr(__import__('backend.collection_handler', fromlist=['']), 'CollectionHandler')

