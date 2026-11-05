from orders import PRODUCTS

def check_num(num):
    try:
        return int(num) > 0
    except ValueError:
        return False

def check_product_id(product_id):
    for p in PRODUCTS:
        if p["id"] == int(product_id):
            return True


