"""
This module provides a build_parser function to build the parser,
and a simple function to process user input
"""

import argparse
from typing import List


def build_parser():
    """
    This function build an ArgumentParser
    Returns:
        an ArgumentParser instance
    """

    parser = argparse.ArgumentParser(prog="restaurants query program",
                                     description="The program is used to \
                                        query the restaurants given a UK postcode")

    parser.add_argument('-s', '--search', type=str,
                        help="search command followed by a postcode.\
                            Usage: --search/-s <POSTCODE>")
    parser.add_argument('-q', '--quit', action='store_true',
                        help="quit the program. Usage: -q/--quit")

    return parser


def split_input(arg_str: str) -> List[str]:
    """
    split the user input string to a list of arguments
    Args:
        input: str represents user input
    Returns:
        a list of arguments
    """
    return arg_str.split()
