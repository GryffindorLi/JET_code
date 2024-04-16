import requests
import json
from typing import List, Dict
from restaurant import Restaurant


def select_json_field(restaurants: List[Dict]):
    return [Restaurant(info) for info in restaurants]

def main(postcode="EC4M7RF"):
    # postcode = input("Please input the postcode you would like to query:\n>>> ")
    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"

    response = requests.get(url=url)

    if response.status_code == 200:
        data = response.json()
    else:
        with open("./fake.json", "r", encoding="utf-8") as f:
            data = json.load(f)

    print(data['restaurants'][:10])

if __name__ == "__main__":
    main()