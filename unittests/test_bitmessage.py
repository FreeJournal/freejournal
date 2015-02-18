import unittest
import sys
import os

class TestBitmessage(unittest.TestCase):
    def setUp(self):
        pass

    def test_startup_success(self):
        try:
            bitmessage = Bitmessage()
        except:
            self.fail("An exception was raised establishing a Bitmessage connection")

if __name__ == '__main__':
    sys.path.append("../bitmessage/")
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.insert(1, path)
    from bitmessage.bitmessage import Bitmessage

    suite = unittest.TestLoader().loadTestsFromTestCase(TestBitmessage)
    unittest.TextTestRunner(verbosity=2).run(suite)