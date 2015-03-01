import unittest
from timestampfile import timestampfile


class TestTimeStamp(unittest.TestCase):


    def test_connection(self):
        testobj = timestampfile("444e6885f143a8b58b04c897f606b5ea826ff8aa42884f92e66d0a16ea0e29c8")
        value = testobj.request_timestamp()
        self.assertEqual(500000, value['price'])
        return 0


    def test_check(self):
        testobj = timestampfile("783701f7599830824fa73488f80eb79894f6f14203264b6a3ac3f0a14012c25f")
        value = testobj.check_TimeStamp()
        self.assertTrue( value['timestamp'])
        self.assertNotEqual(value['time'], "")
        self.assertNotEqual(value['Transaction'],"")
        return 0


if __name__ == '__main__':
    unittest.main()
