import unittest
from global_imports import Collection, CollectionHandler


class TestCollectionHandler(unittest.TestCase):

    def setUp(self):
        self.test_handler = CollectionHandler()

    def tearDown(self):
        self.test_handler = None

    def test_import_collection(self):
        test = self.test_handler.import_collection("BM-2cXbNb5UVcZndcQL6yrhm1iceGyX1KDKK5")
        #self.assertIsInstance(test, Collection)
        #self.assertEqual(test.title, "test title2")

suite = unittest.TestLoader().loadTestsFromTestCase(TestCollectionHandler)
unittest.TextTestRunner(verbosity=2).run(suite)