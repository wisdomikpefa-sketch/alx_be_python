# shopping_list_manager.py

def main():
    shopping_list = []

    while True:
        # Display the menu
        print("\nShopping List Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View shopping list")
        print("4. Exit")

        # Get user input
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty.")

        elif choice == "2":
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' was not found in your shopping list.")

        elif choice == "3":
            if shopping_list:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == "4":
            print("Exiting Shopping List Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
