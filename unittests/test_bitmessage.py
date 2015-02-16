import unittest
import sys

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
    from bitmessage.bitmessage import Bitmessage

    suite = unittest.TestLoader().loadTestsFromTestCase(TestBitmessage)
    unittest.TextTestRunner(verbosity=2).run(suite)