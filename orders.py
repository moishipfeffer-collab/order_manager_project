PRODUCTS = [
    {"id":1, "name":"Keyboard", "price":120,},
    {"id":2, "name":"Mouse", "price":80},
    {"id":3, "name":"Monitor", "price":900},
    {"id":4, "name":"Headphones", "price":200},
    {"id":5, "name":"USB Cable", "price":30}
    
]
FIVE_PERCENT = 300
TEN_PERCENT = 700
FIFTEEN_PERCENT = 1500



def calc_price(product_id,amount):
    price = 0
    for product in PRODUCTS:
        if product["id"] == product_id:
            price = int(product["price"]) * amount
    return price


def calc_discount(price):
    if price < FIVE_PERCENT:
        return price 
    elif price < TEN_PERCENT:
        return price *(1 - 5 / 100) 
    elif price < FIFTEEN_PERCENT:
        return price * (1 - 10 / 100)
    else:
        return price * (1 - 15 / 100) 

def create_item(product_id,amount):
    items = {"product_id": product_id,"quantity":amount}
    return items
    
def create_order(counter, items, total, status):
    order = {"id": counter +1, "items":items, "total":total, "status":status}
    return order

def get_orders_num(orders):
    return len(orders)

def get_income(orders):
    income = 0
    for order in orders:
        if order["status"] == "closed":
            income += order["total"]
    return income

def get_most_expensive_order(orders):
    highest = 0
    highest_order = ""
    for order in orders:
        if int(order["total"]) > highest:
            highest = order["total"]
            highest_order = order
    return highest_order

def sort_orders(orders):
    sorted_orders = sorted(orders,key=lambda o: o["total"],reverse=True)
    return sorted_orders

def get_3_expensive_orders(sorted_orders):
    return sorted_orders[:3]

def check_if_3(three_expensive):
    if len(three_expensive) == 3:
        return True
    return False