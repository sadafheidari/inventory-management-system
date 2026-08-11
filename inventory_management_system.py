
import json

inventory = []

def display_menu():
    print("=" * 50)
    print("Menu Options")
    print("=" * 50)
    print("1. Add Product")
    print("2. View Inventory")
    print("3. Search Product")
    print("4. Delete Product")
    print("5. Update product")
    print("6. Inventory Statistics")
    print("7. Save information")
    print("8. Exit")


def get_user_choice():
    return input("Please select an option from the menu: ").strip()

def add_product():
    code = input("please enter the product code reference: ").strip()
    for product in inventory:
        if product["code"] == code:
            print("A product with this code already exists.")
            return

    name =input(" please enter your product name: ").strip()
    category =input("please enter the product category: " ).strip()
    weight =input("please enter the product weight: ").strip()
    while True:
        try:
            quantity = int(input("Please enter the product available quantity: "))

            if quantity < 0:
                print("Quantity cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid whole number.")
    material =input("please enter the product material: ").strip()
    origin =input("please enter the product origin: ").strip()
    while True:
        try:
            price = float(input("Please enter the product price: "))

            if price < 0:
                print("Price cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid price.")

    product= {"name":name,
              "code":code,
              "category":category,
              "weight":weight,
              "quantity":quantity,
              "material":material,
              "origin":origin,
              "price":price
              }
    inventory.append(product)
    print("\nProduct added successfully.")


def view_inventory():
    if inventory :
        print("\nInventory:")
        for product in inventory:
            print(f"name: {product['name']},"
                  f"code: {product['code']},"
                  f"category: {product['category']},"
                  f"weight: {product['weight']},"
                  f"quantity: {product['quantity']},"
                  f"material: {product['material']},"
                  f"origin: {product['origin']},"
                  f"price: {product['price']}")

    else:
        print("\nInventory is empty.")


def search_product():
    search = input("please enter the product code: ").strip()
    found = False
    for product in inventory:
        if product["code"] == search:
            found = True
            print("-" * 40)
            print(f"Name     : {product['name']}")
            print(f"Code     : {product['code']}")
            print(f"Category : {product['category']}")
            print(f"Weight   : {product['weight']}")
            print(f"Quantity : {product['quantity']}")
            print(f"Material : {product['material']}")
            print(f"Origin   : {product['origin']}")
            print(f"Price    : ${product['price']}")
            break
    if not found:
        print("Product not found.")


def delete_product():
    delete = input("please enter the product code: ").strip()
    found = False
    for product in inventory:
        if product["code"] == delete:
            found = True
            inventory.remove(product)
            print("Product deleted successfully.")
            break
    if not found:
        print("Product not found.")

def update_product():
    code = input("Please enter the product code to update: ").strip()

    for product in inventory:
        if product["code"] == code:

            product["name"] = input("Please enter the new product name: ").strip()
            product["category"] = input("Please enter the new category: ").strip()
            product["weight"] = input("Please enter the new weight: ").strip()
            product["material"] = input("Please enter the new material: ").strip()
            product["origin"] = input("Please enter the new origin: ").strip()

            while True:
                try:
                    quantity = int(input("Please enter the new quantity: "))

                    if quantity < 0:
                        print("Quantity cannot be negative.")
                        continue

                    product["quantity"] = quantity
                    break

                except ValueError:
                    print("Please enter a valid whole number.")

            while True:
                try:
                    price = float(input("Please enter the new price: "))

                    if price < 0:
                        print("Price cannot be negative.")
                        continue

                    product["price"] = price
                    break

                except ValueError:
                    print("Please enter a valid price.")

            print("Product updated successfully.")
            return

    print("Product not found.")



def save_inventory():
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully.")


def load_inventory():
    global inventory

    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file)

    except FileNotFoundError:
        inventory = []

    except json.JSONDecodeError:
        inventory = []
        print("Inventory file is invalid. Starting with an empty inventory.")

def inventory_statistics():
    total_products = len(inventory)
    total_quantity = 0
    total_value = 0

    for product in inventory:
        total_quantity += product["quantity"]
        total_value += product["price"] * product["quantity"]

    print("-" * 40)
    print(f"Total Product Types: {total_products}")
    print(f"Total Quantity: {total_quantity}")
    print(f"Total Inventory Value: ${total_value:.2f}")
        
def main():
    while True:
        display_menu()
        user_choice = get_user_choice()

        if user_choice == "1":
            add_product()
        elif user_choice == "2":
            view_inventory()
        elif user_choice == "3":
            search_product()
        elif user_choice == "4":
            delete_product()
        elif user_choice == "5":
            update_product()
        elif user_choice == "6":
            inventory_statistics()
        elif user_choice == "7":
            save_inventory()
        elif user_choice == "8":
            print("Thank you for using Inventory Management System.")
            break
        else:
            print("Please select a valid option.")

load_inventory()
main()