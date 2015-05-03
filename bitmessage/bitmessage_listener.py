from controllers.controller import Controller
from config import MAIN_CHANNEL_ADDRESS, LISTEN_PERIOD
from async import repeat_periodic, wait_for_interrupt, run_as_thread
from time import sleep

@run_as_thread
def wait_for_join(controller):
    controller.join_downloads()


def exit_func(controller):
    print ""
    if controller.alive_downloads():
        print "Downloads in progress, please wait for them to finish. Press ctrl+c again to cancel downloads."
        try:
            t = wait_for_join(controller)
            while t.is_alive():
                sleep(0.1)
            print "Exited safely."
        except (KeyboardInterrupt, SystemExit):
            print ""
            print "Cancelling downloads and exiting."
            exit(1)
    else:
        print "Exiting listener."


def get_collections():
    """Get collections from the main channel"""

    collection_handler = Controller()
    wait_for_interrupt(exit_func, do_import(collection_handler), args=[collection_handler])


@repeat_periodic(LISTEN_PERIOD)
def do_import(collection_handler):
    collection_handler.import_collection(MAIN_CHANNEL_ADDRESS)
