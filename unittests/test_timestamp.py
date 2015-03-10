import unittest
from timestamp.timestampfile import TimestampFile


class TestTimestamp(unittest.TestCase):
    def test_connection(self):
        test_obj = TimestampFile("444e6885f143a8b58b04c897f606b5ea826ff8aa42884f92e66d0a16ea0e29c8")
        value = test_obj.request_timestamp
        self.assertEqual(500000, value['price'])
        return 0

    def test_check(self):
        test_obj = TimestampFile("783701f7599830824fa73488f80eb79894f6f14203264b6a3ac3f0a14012c25f")
        value = test_obj.check_timestamp()
        self.assertTrue(value['timestamp'])
        self.assertNotEqual(value['time'], "")
        self.assertNotEqual(value['Transaction'], "")
        return 0

suite = unittest.TestLoader().loadTestsFromTestCase(TestTimestamp)
unittest.TextTestRunner(verbosity=2).run(suite)
