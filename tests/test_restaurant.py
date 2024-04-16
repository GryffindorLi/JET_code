import unittest

from src.restaurant import Restaurant


class TestRestaurant(unittest.TestCase):
    def setUp(self):
        self.restaurant_info = {
            'name': 'My Favorite Restaurant',
            'cuisines': [{'name': 'Italian'}, {'name': 'Peruvian'}],
            'rating': {'starRating': 4.5, 'count': 17},
            'address': {'firstLine': '123 Main St', 'city': 'London', 'postalCode': '12345'}
        }

        # Create a Restaurant instance for testing
        self.restaurant = Restaurant(self.restaurant_info)

    def test_name(self):
        self.assertEqual(self.restaurant.name, 'My Favorite Restaurant')

    def test_cuisines(self):
        self.assertEqual(self.restaurant.cuisines, ['Italian', 'Peruvian'])

    def test_rating(self):
        self.assertEqual(self.restaurant.rating, (4.5, 17))

    def test_address(self):
        self.assertEqual(self.restaurant.address, '123 Main St, London, 12345')


if __name__ == '__main__':
    unittest.main()
