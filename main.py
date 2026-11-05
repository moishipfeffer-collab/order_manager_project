from run_app import show_menu,creat_order_flow,find_order_by_id
from storage import load_from_json

def main():
    orders = load_from_json()
    choise = show_menu()
    if choise == "1":
        creat_order_flow(orders)
    elif choise == "2":
        print(orders)
    elif choise == "3":
        find_order_by_id(orders)
main()
        
