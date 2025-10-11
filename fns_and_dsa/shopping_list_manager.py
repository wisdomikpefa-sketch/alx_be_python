# Shopping List Manager
def display_menu():
    print("\n--- Shopping List Menu ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View shopping list")
    print("4. Exit")  

def main():
    shopping_list = []  # Start with an empty list

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            # Add item
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty.")

        elif choice == "2":
            # Remove item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in your shopping list.")

        elif choice == "3":
            if shopping_list:
                print("Your Shopping List:")
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is currently empty.")

        elif choice == "4":
            # Exit
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")