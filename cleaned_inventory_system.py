"""Inventory management system module.

This module provides basic functionality to add, remove, save,
and load inventory data while maintaining logs and safe file handling.
"""

import json
import logging
from datetime import datetime

logging.basicConfig(
    filename='inventory.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

stock_data = {}


def add_item(item=None, qty=0, logs=None):
    """Add an item and quantity to the inventory."""
    if not item or not isinstance(qty, int):
        logging.warning("Invalid input for add_item: %s, %s", item, qty)
        return
    if logs is None:
        logs = []
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a quantity of an item from the inventory."""
    try:
        if item in stock_data:
            stock_data[item] -= qty
            if stock_data[item] <= 0:
                del stock_data[item]
        else:
            logging.warning("Tried to remove nonexistent item: %s", item)
    except KeyError as error:
        logging.error("KeyError while removing item: %s", error)
    except TypeError as error:
        logging.error("TypeError while removing item: %s", error)


def get_qty(item):
    """Return the quantity of the given item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file and return it."""
    try:
        with open(file, "r", encoding="utf-8") as file_handle:
            data = json.load(file_handle)
            return data
    except (FileNotFoundError, json.JSONDecodeError) as error:
        logging.error("Error loading data: %s", error)
        return {}


def save_data(file="inventory.json"):
    """Save current inventory data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as file_handle:
            json.dump(stock_data, file_handle, indent=4)
    except OSError as error:
        logging.error("Error saving data: %s", error)


def print_data():
    """Display the current inventory in a readable format."""
    logging.info("Printing inventory data")
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items below the given threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main execution block for the inventory system."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    loaded_data = load_data()
    if loaded_data:
        stock_data.clear()
        stock_data.update(loaded_data)
    print_data()


if __name__ == "__main__":
    main()
