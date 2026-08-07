inventory = []

def display_menu():
    print("=" * 50)
    print("Menu Options")
    print("=" * 50)
    print("1. Add Product")
    print("2. View Inventory")
    print("3. Search Product")
    print("4. Return Product")
    print("5. Save information")
    print("6. Exit")


def get_user_choice():
    return input("Please select an option from the menu: ").strip()

def add_product():
    name =input(" please enter your product name: ").strip()
    code =input("please enter the product code reference: ").strip()
    category =input("please enter the product category: " ).strip()
    weight =input("please enter the product weight: ").strip()
    quantity =int(input("please enter the product available quantity: "))
    material =input("please enter the product material: ").strip()
    origin =input("please enter the product origin: ").strip()
    price =float(input("please enter the product price: "))

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
    search =input("please enter the product code: ").strip()
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
        elif user_choice == "6":
            print("Thank you for using Inventory Management System.")
            break
        else:
            print("Feature coming soon...")


main()