from global_imports import Controller, MAIN_CHANNEL_ADDRESS


def get_collections():
    """Get collections from the main channel"""

    collection_handler = Controller()
    new_collection = True
    while new_collection:
       collection_handler.import_collection(MAIN_CHANNEL_ADDRESS)


if __name__ == '__main__':
    get_collections()