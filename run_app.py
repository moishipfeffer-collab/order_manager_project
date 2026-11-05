from inputs import get_product_id,get_amount,check_another_order,get_order_id
from orders import calc_price,calc_discount,create_item,create_order
from storage import add_to_json,save_to_json

def show_menu():
    while True:
        choise = input("========== ORDER MANAGER ==========\n1. Create order\n" \
        "2. Show all orders\n3. Find order by ID\n4. Close order" \
        "\n5. Show sales report\n0. exit\nchoose option: ")
        if choise in ["1","2","3","4","5","0"]:
            return choise
        print("not valid choise")

# option 1 create order

def creat_order_flow(orders):
    total_price = 0
    items = []
    if orders:
        counter = orders[-1]["id"]
    else:
        counter = 0
    while True:
        product_id = get_product_id()
        amount = get_amount()
        price = calc_price(int(product_id),int(amount))
        total_price += calc_discount(price)
        item = create_item(product_id,amount)
        items.append(item)
        if not check_another_order():
            order = create_order(counter,items,total_price,"open")
            updated_orders = add_to_json(orders,order)
            save_to_json(updated_orders)
            return order
# option 3 

def find_by_id(orders,order_id):
    for order in orders:
        if order["id"] == int(order_id):
            return order
    return False
        
def find_order_by_id(orders):
    order_id = get_order_id(orders)
    order = find_by_id(orders,order_id)
    if order:
        print(order)
    else:
        print("order not found")
