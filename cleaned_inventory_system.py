
import json
import logging
from datetime import datetime

logging.basicConfig(filename='inventory.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

stock_data = {}

def add_item(item=None, qty=0, logs=None):
    if not item or not isinstance(qty, int):
        logging.warning("Invalid input for add_item: %s, %s", item, qty)
        return
    if logs is None:
        logs = []
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def remove_item(item, qty):
    try:
        if item in stock_data:
            stock_data[item] -= qty
            if stock_data[item] <= 0:
                del stock_data[item]
        else:
            logging.warning(f"Tried to remove nonexistent item: {item}")
    except KeyError as e:
        logging.error(f"KeyError while removing item: {e}")
    except TypeError as e:
        logging.error(f"TypeError while removing item: {e}")

def get_qty(item):
    return stock_data.get(item, 0)

def load_data(file="inventory.json"):
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Error loading data: {e}")
        stock_data = {}

def save_data(file="inventory.json"):
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f)
    except OSError as e:
        logging.error(f"Error saving data: {e}")

def print_data():
    logging.info("Printing inventory data")
    print("Items Report")
    for i, q in stock_data.items():
        print(f"{i} -> {q}")

def check_low_items(threshold=5):
    return [i for i, q in stock_data.items() if q < threshold]

def main():
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()

if __name__ == "__main__":
    main()
