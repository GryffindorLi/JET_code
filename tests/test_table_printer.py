import unittest

from src.restaurant import Restaurant
from src.table_printer import TablePrinter


class TestTablePrinter(unittest.TestCase):
    def setUp(self):
        self.json = {
            'name': 'my favorite',
            'cuisines': [
                {'uniqueName': 'Italian'},
                {'uniqueName': 'Peruvian'}
            ],
            'rating': {
                'starRating': 4.5
            },
            'address': {
                "city": "London",
                "firstLine": "40a Museum Street",
                "postalCode": "WC1A 1LU",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        -0.125679,
                        51.517856
                    ]
                }
            }
        }

        self.restaurant = Restaurant(self.json)
        self.printer = TablePrinter()

    def test_format_field(self):
        f = self.printer._format_field(self.restaurant)
        target = ('my favorite', '4.5',
                  'Italian, Peruvian', '40a Museum Street, London, WC1A 1LU')
        self.assertTupleEqual(f, target)
