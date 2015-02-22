import unittest
from unittests.test_cache import TestCache

suite = unittest.TestLoader().loadTestsFromTestCase(TestCache)
unittest.TextTestRunner(verbosity=2).run(suite)
