from backend.collection_handler import CollectionHandler
from config import MAIN_CHANNEL_ADDRESS


def get_collections():
    """Get collections from the main channel"""

    collection_handler = CollectionHandler()
    new_collection = True
    while new_collection:
        collection_handler.import_collection(MAIN_CHANNEL_ADDRESS)
