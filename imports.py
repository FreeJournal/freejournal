import os
import sys

from config import *
from cache.cache import *

Bitmessage = getattr(__import__('bitmessage.bitmessage', fromlist=['']), 'Bitmessage')
Collection = getattr(__import__('models.collection', fromlist=['']), 'Collection')
Document = getattr(__import__('models.document', fromlist=['']), 'Document')
Keyword = getattr(__import__('models.keyword', fromlist=['']), 'Keyword')
FJMessage = getattr(__import__('backend.datastructures.fj_message', fromlist=['']), 'FJMessage')
Controller = getattr(__import__('backend.controller', fromlist=['']), 'Controller')



