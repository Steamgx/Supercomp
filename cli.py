import sys
from models import create_client, create_product, create_order, get_clients, get_products, get_orders, get_client_orders

def main():
    print("1. Create Client")
    print("2. Create Product")
    print("3. Create Order")
    print("4. Get Clients")
    print("5. Get Products")
    print("6. Get Orders")
    print("7. Get Client Orders")
    print("8. Exit")

    input_ = input("Enter your choice to proceed: ")

    if input_ == '1':
        name = input("Enter client name: ")
        age = int(input("Enter client age: "))
        address = input("Enter client address: ")
        create_client(name, age, address)
        print(f'Client {name} has been created')

    elif input_ == '2':
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        create_product(name, price)
        print(f'Product {name} has been created')

    elif input_ == '3': 
        client_id = int(input("Enter client ID: "))
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))
        total = float(input("Enter total price: "))
        create_order(client_id, product_id, quantity, total)
        print(f'Order created for client {client_id} with product {product_id}')

    elif input_ == '4':
        clients = get_clients() or []
        for client in clients:
            print(client)

    elif input_ == '5':
        products = get_products() or []
        for product in products:
            print(product)

    elif input_ == '6':
        orders = get_orders() or []
        for order in orders:
            print(order)

    elif input_ == '7':
        client_id = int(input("Enter client ID: "))
        orders = get_client_orders(client_id) or []
        for order in orders:
            print(order)

    elif input_ == '8': 
        print("Bye!")
        sys.exit()

# Ensure the script runs the main function
if __name__ == "__main__":
    main()
