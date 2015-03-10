import unittest
from backend.datastructures.fj_message import FJMessage


class TestFJMessage(unittest.TestCase):

    def setUp(self):
        self.test_fj_message = FJMessage(1, 'BM-2cXbNb5UVcZndcQL6yrhm1iceGyX1KDKK5', 'fake')

    def tearDown(self):
        self.test_fj_message = None

    def test_create_collection(self):
        self.assertIsInstance(self.test_fj_message, FJMessage)
        self.assertEqual(self.test_fj_message.type_id, 1)
        self.assertEqual(self.test_fj_message.original_sender, 'BM-2cXbNb5UVcZndcQL6yrhm1iceGyX1KDKK5')
        self.assertEqual(self.test_fj_message.payload, 'fake')

    # def test_generate_signature(self):
    #     self.assertEqual(self.test_fj_message.signature, '')
    #     self.test_fj_message.to_json()
    #     self.assertEqual(self.test_fj_message.signature,
    #                      "588e09c14c2ca5256780be346a3c8a1214c5e61af7c7fb9471cdd43800d561c8")
    #     self.test_fj_message.payload = 'notfake?'
    #     self.test_fj_message.to_json()
    #     self.assertEqual(self.test_fj_message.signature,
    #                      '7f6395bbe549a884b6ea09fb0d48e4182a648678b1b713a45f08ffe5f73dd3a7')

    # def test_to_json(self):
    #     test_json_encode = self.test_fj_message.to_json()
    #     self.assertIn('"original_sender": "BM-2cXbNb5UVcZndcQL6yrhm1iceGyX1KDKK5", "payload": "fake", '
    #                   '"protocol": "FJ1.0", "signature": ""', test_json_encode)


suite = unittest.TestLoader().loadTestsFromTestCase(TestFJMessage)
unittest.TextTestRunner(verbosity=2).run(suite)
