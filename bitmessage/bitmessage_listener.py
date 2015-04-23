from controllers.controller import Controller
from config import MAIN_CHANNEL_ADDRESS, LISTEN_PERIOD
from async import repeat_periodic, wait_for_interrupt


def exit_func():
    print ""
    print "exiting."


def get_collections():
    """Get collections from the main channel"""

    collection_handler = Controller()

    wait_for_interrupt(exit_func, do_import(collection_handler))


@repeat_periodic(LISTEN_PERIOD)
def do_import(collection_handler):
    collection_handler.import_collection(MAIN_CHANNEL_ADDRESS)
