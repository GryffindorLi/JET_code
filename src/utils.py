import re
from typing import Dict, List

from src.restaurant import Restaurant

TEMPLATE = r'^[A-Za-z]{1,2}\d[A-Za-z\d]?\s?\d[A-Za-z]{2}$'


def check_postcode(postcode: str) -> bool:
    """
    check if the given postcode is a valid UK postcode
    Args:
        postcode: a string represents the postcode
    Returns:
        True or False
    """
    match = re.search(TEMPLATE, postcode)

    return match is not None


def select_json_field(restaurants: List[Dict]) -> List[Restaurant]:
    """
    extract related field to Restaurant class
    Args:
        restaurants: a list of json dict
    Returns:
        A list of Restaurant instance
    """
    return [Restaurant(info) for info in restaurants]
