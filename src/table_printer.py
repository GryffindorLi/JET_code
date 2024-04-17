"""
This module provide a TablePrinter class that format the data into a table
and print it in the console.
"""
from typing import List, Tuple

import rich
import rich.box
from rich.console import Console
from rich.table import Table

from src.restaurant import Restaurant


class TablePrinter:
    """
    A class that print table in the console.
    """

    def __init__(self):
        self.console = Console()

    def _format_field(self, restaurant: Restaurant) -> Tuple[str, str, str, str]:
        """
        extract the data in a Restaurant instance to a tuple
        Args:
            restaurant: an instance of Restaurant.
        Returns:
            a tuple of four field (name, rating, cuisines, address)
        """
        rating = str(restaurant.rating)
        cuisines = ", ".join(restaurant.cuisines)

        return (restaurant.name, rating, cuisines, restaurant.address)

    def print_table(self, restaurants: List[Restaurant], postcode: str):
        """
        a function that prints the table in the console.
        Args:
            restaurants: a list of Restaurant instance.
            postcode: a string represents the postcode of current query.
        """
        table = Table(title=f"First 10 restaurants near {postcode}",
                      show_lines=True, box=rich.box.DOUBLE_EDGE)
        table.add_column("Name", justify="center", vertical="middle")
        table.add_column("Ratings", justify="center", vertical="middle")
        table.add_column("Cuisines", justify="center", vertical="middle")
        table.add_column("Address", justify="center", vertical="middle")
        for restaurant in restaurants:
            table.add_row(*self._format_field(restaurant))

        self.console.print(table)
