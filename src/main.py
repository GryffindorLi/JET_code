import json

import requests

from src.utils import check_postcode, select_json_field


def main(postcode: str = "EC4M7RF"):
    # postcode = input("Please input the postcode you would like to query:\n>>> ")

    if not check_postcode(postcode=postcode):
        raise ValueError("The postcode must be a valid UK postcode.")

    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{
        postcode}"

    response = requests.get(url=url)

    if response.status_code == 200:
        data = response.json()
    else:
        with open("./fake.json", "r", encoding="utf-8") as f:
            data = json.load(f)

    top10_data = select_json_field(data['restaurants'][:10])
    print(top10_data)


if __name__ == "__main__":
    main()
