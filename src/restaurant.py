from typing import List, Dict

class Restaurant:
    def __init__(self, restaurant_info: Dict):
        self._name = restaurant_info['name']
        self._cuisines = self._extract_cuisines(restaurant_info['cuisines'])
        self._rating = restaurant_info['rating']['starRating']
        self._address = self._extract_address(restaurant_info['address'])

    @property
    def name(self):
        return self._name
    
    @property
    def cuisines(self):
        return self._cuisines
    
    @property
    def rating(self):
        return self._rating
    
    @property
    def address(self):
        return self._address

    def _extract_cuisines(self, cuisines: List[Dict]) -> List[str]:
        return list(map(lambda x: x['name'], cuisines))
    
    def _extract_address(self, address_info: Dict) -> str:
        return f"{address_info['firstLine']}, {address_info['city']}, {address_info['postalCode']}"