import unittest
from global_imports import Collection, CollectionHandler


class TestCollectionHandler(unittest.TestCase):

    def setUp(self):
        self.test_handler = CollectionHandler()

    def tearDown(self):
        self.test_handler = None

    def test_import_collection(self):
        test = self.test_handler.import_collection("BM-2cVGRPC25r5pXTbEHPbNJw5U4PJPBG2UJu")
        #self.assertEqual(True, test)

suite = unittest.TestLoader().loadTestsFromTestCase(TestCollectionHandler)
unittest.TextTestRunner(verbosity=2).run(suite)