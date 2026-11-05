from run_app import show_menu,creat_order_flow,find_order_by_id
from run_app import close_order,show_sales_report,show_orders
from storage import load_from_json

def main():
    while True:
        orders = load_from_json()
        choise = show_menu()
        if choise == "1":
            creat_order_flow(orders)
        elif choise == "2":
            show_orders(orders)
        elif choise == "3":
            find_order_by_id(orders)
        elif choise == "4":
            close_order(orders)
        elif choise == "5":
            show_sales_report(orders)
        elif choise == "0":
            print("goodby!")
            break

main()
        
