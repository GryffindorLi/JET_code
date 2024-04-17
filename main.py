import json

import requests

from src.parser import build_parser, split_input
from src.utils import check_postcode, select_json_field


def main(postcode: str = "EC4M7RF", debug: bool = False):
    parser = build_parser()
    cmd = input("Please input the command."
                "'--search' for querying the UK postcode"
                "(no space in between). "
                "'--quit' to quit the program:\n>>> ")

    args = parser.parse_args(split_input(cmd))

    if args.quit:
        return

    if not check_postcode(args.search):
        raise ValueError("The postcode must be a valid UK postcode.")

    if not debug:
        url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{
            postcode}"
        response = requests.get(url=url, timeout=2.0)

        if response.status_code == 200:
            data = response.json()
    else:
        with open("./fake.json", "r", encoding="utf-8") as f:
            data = json.load(f)

    top10_data = select_json_field(data['restaurants'][:10])
    print(top10_data)


if __name__ == "__main__":
    main(debug=True)
