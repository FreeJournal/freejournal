import unittest
from async import run_as_thread, repeat_periodic
from time import sleep

@repeat_periodic(0.5)
def periodic_func(l):
    l.append("test")

@run_as_thread
def thread_func(l):
    l.append("test")
    sleep(0.5)
    l.append("test")
    sleep(0.5)


class TestAsync(unittest.TestCase):
    def test_repeat_periodic(self):
        l = []
        ev = periodic_func(l)
        sleep(1.7)
        ev.set()
        self.assertEquals(len(l), 3)
        l = []
        ev = periodic_func()
        sleep(0.1)
        ev.set()
        self.assertEquals(len(l), 0)

    def test_run_as_thread(self):
        l = []
        t = thread_func(l)
        sleep(0.25)
        self.assertEquals(len(l), 1)
        sleep(1.25)
        self.assertEquals(len(l), 2)
        t.join()
        self.assertFalse(t.is_alive())
