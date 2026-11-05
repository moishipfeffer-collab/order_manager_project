import json 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

orders_file = Path(__file__).parent / "orders.json"

def load_from_json():
    if not orders_file.exists():
        return []
    try:
        with open(orders_file,"r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        logging.error("the json file has a problem")
        return []

def add_to_json(orders:list,order):
    orders.append(order)
    return orders

def save_to_json(orders):
    with open(orders_file,"w") as file:
        json.dump(orders,file,indent=4)