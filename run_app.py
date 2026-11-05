from inputs import get_product_id,get_amount,check_another_order,get_order_id
from orders import calc_price,calc_discount,create_item,create_order,PRODUCTS,sort_orders
from orders import get_income,get_3_expensive_orders,get_most_expensive_order,get_orders_num,check_if_3
from storage import add_to_json,save_to_json
from validations import check_if_open

import logging
logging.basicConfig(level=logging.INFO,format="%(levelname)s %(message)s")

def show_menu():
    while True:
        choise = input("\n========== ORDER MANAGER ==========\n1. Create order\n" \
        "2. Show all orders\n3. Find order by ID\n4. Close order" \
        "\n5. Show sales report\n0. exit\nchoose option: ")
        if choise in ["1","2","3","4","5","0"]:
            return choise
        print("not valid choise")

# option 1 create order
def show_products():
    print("\nthose are the available products:")
    for product in PRODUCTS:
        print(product)

def creat_order_flow(orders):
    total_price = 0
    items = []
    price = 0
    if orders:
        counter = orders[-1]["id"]
    else:
        counter = 0
    show_products()
    while True:
        product_id = get_product_id()
        amount = get_amount()
        price += calc_price(int(product_id),int(amount))
        item = create_item(product_id,amount)
        items.append(item)
        if not check_another_order():
            total_price = calc_discount(price)
            order = create_order(counter,items,total_price,"OPEN")
            updated_orders = add_to_json(orders,order)
            save_to_json(updated_orders)
            logging.info("order created successfully")
            return 
        
#option 2 show orders

def show_orders(orders):
    if not orders:
        print("no orders yet!")
    else:
        print(orders)

# option 3 find order by id

def find_by_id(orders,order_id):
    for order in orders:
        if order["id"] == int(order_id):
            return order
    return False
        
def find_order_by_id(orders):
    if not orders:
        print("no orders yet!")
        return 
    order_id = get_order_id()
    order = find_by_id(orders,order_id)
    if order:
        print(order)
    else:
        print("order not found")

# option 4 close order 

def close_order(orders):
    if not orders:
        print("no orders yet! ")
        return
    order_id = get_order_id()
    order = find_by_id(orders,order_id)
    if not order:
        print("order not found")
    else:
        if check_if_open(order):
            order["status"] = "CLOESED"
            logging.info("the order has closed successfully")
        else:
            print("the order is closed already")
        save_to_json(orders)

# option 5 

def show_sales_report(orders):
    if not orders:
        print("no orders yet!")
        return
    orders_num = get_orders_num(orders)
    income = get_income(orders)
    most_expensive = get_most_expensive_order(orders)
    sorted_orders = sort_orders(orders)
    three_expensive = get_3_expensive_orders(sorted_orders)
    print("\n==== sales report ====")
    print(f"orders number: {orders_num}")
    print(f"income: {income}")
    print(f"most expencive order:\n{most_expensive}")
    if check_if_3(three_expensive):
        print(f"three expensive orders:\n{three_expensive}")
    else:
        print(f"the most expensivest orders:\n{three_expensive}")

     
    