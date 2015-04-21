from threading import Thread, Timer
from functools import wraps
from time import sleep


def run_as_thread(func):
    """
    Decorator for making a function run as a new thread
    :param func: the function to run
    :return: the resulting thread object
    """
    @wraps(func)
    def thread_func(*args, **kwargs):
        thread = Thread(target=func, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
        return thread

    return thread_func

@run_as_thread
def run_periodic(func, period, args=[], kwargs={}):
    """
    Calls a function once per period
    :param func: the function to call
    :param period: the time in seconds between calls
    """
    while True:
        func(*args, **kwargs)
        sleep(period)
