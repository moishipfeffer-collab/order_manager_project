from validations import check_num,check_product_id

import logging
logging.basicConfig(level=logging.INFO,format="%(levelname)s %(message)s")

def get_product_id():
    while True:
        product_id = input("\nenter product id: ")
        if not check_num(product_id):
            logging.error("the id must be a positive number ")
            continue
        elif not check_product_id(product_id):
            logging.error("product id not found")
            continue
        return product_id

def get_amount():
    while True:
        amount = input("enter amount: ")
        if check_num(amount):
            return amount
        logging.error("the amount must be a positive number")

def check_another_order():
    while True:
        another_order = input("do you want to order sum more?\n1. yes\n2. no\nchoose: ")
        if another_order in ["1","2"]:
            if another_order == "1":
                return True
            return
        logging.error("not valid choise")

def get_order_id():
    while True:
        order_id = input("enter order id: ")
        if check_num(order_id):
            return order_id
        logging.error("the id must be a positive number")
            


