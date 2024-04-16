import unittest

from src.utils import check_postcode


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.valid_postcode = ['SW1A 1AA', 'L4 0TH', 'EH1 1RE']
        self.invalid_postcode = ['1AA 1AA', 'ABC1 4CF', 'EB4 B7B']

    def test_valid_postcode(self):
        for valid_code in self.valid_postcode:
            self.assertTrue(check_postcode(valid_code))

    def test_invalid_postcode(self):
        for invalid_code in self.invalid_postcode:
            self.assertFalse(check_postcode(invalid_code))


if __name__ == "__main__":
    unittest.main()
