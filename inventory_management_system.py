inventory = []

def display_menu():
    print("=" * 50)
    print("Menu Options")
    print("=" * 50)
    print("1. Add Product")
    print("2. View Inventory")
    print("3. Return Product")
    print("4. Check requested item")
    print("5. Save information")
    print("6. Exit")


def get_user_choice():
    return input("Please select an option from the menu: ").strip()


def main():
    while True:
        display_menu()
        user_choice = get_user_choice()

        if user_choice == "6":
            print("Thank you for using Inventory Management System.")
            break
        else:
            print("Feature coming soon...")


main()