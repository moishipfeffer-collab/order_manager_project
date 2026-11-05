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
        return price - (price / 100 * 5)
    elif price < FIFTEEN_PERCENT:
        return price - (price / 100 * 10)
    else:
        return price - (price / 100 * 15)

def create_item(product_id,amount):
    items = {"product_id": product_id,"quantity":amount}
    return items
    
def create_order(counter, items, total, status):
    order = {"id": counter +1, "items":items, "total":total, "status":status}
    return order
