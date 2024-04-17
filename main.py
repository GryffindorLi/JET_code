"""
The entrance of the Restaurants query program.
"""
import json
import logging

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
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    if to_console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if to_file:
        file_handler = logging.FileHandler('./logs/logfile.log')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def main(logger: logging.Logger, debug: bool = False):
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
        # args = parser.parse_args(split_input(cmd))

        if args.quit:
            logger.info("Quiting the program......")
            break

        if not check_postcode(args.search):
            logger.error(f"Wrong postcode {args.search}. "
                         "Please provide a valid UK postcode")
            continue

        if not debug:
            url = "https://uk.api.just-eat.io/discovery/uk/restaurants/"\
                f"enriched/bypostcode/{args.search}"
            response = requests.get(url=url, timeout=2.0)

            if response.status_code == 200:
                data = response.json()
        else:
            with open("./fake.json", "r", encoding="utf-8") as f:
                data = json.load(f)

        top10_data = select_json_field(data['restaurants'][:10])
        printer.print_table(top10_data, postcode=args.search)


if __name__ == "__main__":
    lgr = build_logger()
    main(logger=lgr, debug=True)
