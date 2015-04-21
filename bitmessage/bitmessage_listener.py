from controllers.controller import Controller
from config import MAIN_CHANNEL_ADDRESS, LISTEN_PERIOD
from async import run_periodic
from time import sleep


def get_collections():
    """Get collections from the main channel"""

    collection_handler = Controller()
    run_periodic(do_import, LISTEN_PERIOD, args=[collection_handler])
    while True:
        try:
            sleep(0.1)
        except (KeyboardInterrupt, SystemExit):
            exit(0)


def do_import(collection_handler):
    collection_handler.import_collection(MAIN_CHANNEL_ADDRESS)
