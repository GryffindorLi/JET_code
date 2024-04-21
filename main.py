"""
The entrance of the Restaurants query program.
"""
import json
import logging
from functools import lru_cache
from typing import Dict, List, Optional

import requests

from src.parser import build_parser, split_input
from src.table_printer import TablePrinter
from src.utils import check_postcode, select_json_field


def build_logger(to_file: bool = True, to_console: bool = True) -> logging.Logger:
    """
    A function that build up a logger that 
    can print to console and write to file.
    Args:
        to_file: bool, default=True. whether write to file.
        to_console: bool, default=True. whether print to the console.
    Returns:
        a instance of logging.Logger class.
    """
    lgr = logging.getLogger(__name__)
    lgr.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    if to_console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        lgr.addHandler(console_handler)

    if to_file:
        file_handler = logging.FileHandler('logfile.log')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        lgr.addHandler(file_handler)

    return lgr


logger = build_logger()


@lru_cache(maxsize=64)
def get_data(postcode: str) -> Optional[List[Dict]]:
    """
    a function that fetches data from the API and returns all metadata of the first 10 restaurants.
    Use lru_cache to reduce API calls for recently called postcodes.
    Args:
        postcode: a str represents the postcode.
    Returns:
        an Optional[Dict]. If fetch successfully from API or from lru_cache,
        return a list of json dict. Otherwise, return None.
    """
    if not check_postcode(postcode):
        logger.error(f"Wrong postcode {postcode}. "
                     "Please provide a valid UK postcode")
        return
    url = "https://uk.api.just-eat.io/discovery/uk/restaurants/"\
        f"enriched/bypostcode/{postcode}"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
               'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 '
               'Safari/537.36'}
    response = requests.get(url=url, timeout=2.0, headers=headers)

    if response.status_code == 200:
        data = response.json()
        logger.info(f"Successfully fetching data for {postcode}")
        return data['restaurants'][:10]
    logger.warning(f"Fail to fetch data for {
                   postcode}. Status code {response.status_code}")


def main(debug: bool = False):
    """
    The main function of the Restaurants query program.
    Args:
        logger: an instance of logging.Logger class.
        debug: whether in debug mode. If this is True, load data from local json file.
    """
    parser = build_parser()
    printer = TablePrinter()

    logger.info("Please input the command."
                "'--help' or '-h' to see all commands")

    while True:
        cmd = input(">>> ")

        try:
            args = parser.parse_args(split_input(cmd))
        except SystemExit as e:
            logger.error(f"Exit code {e.code}. "
                         "Unrecognized argument. Please check your "
                         "input arguments, or use '-h' for help.")
            continue

        if args.quit:
            logger.info("Quiting the program......")
            break

        data = get_data(args.search)
        
        if not data:
            logger.info(f"No data is available for {args.search}")
            continue

        top10_restaurants = select_json_field(data)
        printer.print_table(top10_restaurants, postcode=args.search)


if __name__ == "__main__":
    main(debug=False)
