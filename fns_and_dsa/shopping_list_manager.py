# shopping_list_manager.py
def main():
    shopping_list = []  # Start with an empty list:
    while True:
        print("\n--- Shopping List Menu ---")
        print("1. Add item")
        print("2. Remove item")
        print("3. View shopping list")
        print("4. Exit")

def display_menu():
    while True:
        choice = input("Enter your choice (1-4): ").strip().lower()
        print("shopping_list_manager.")

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list manager.")

        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list manager.")

            else:
                print(f"'{item}' is not in your shopping list manager.")
        elif choice == '3':
            if shopping_list:
                print("Your shopping list manager:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")

            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            print("Exiting the shopping list manager. Goodbye!")
            break

        else:
            print("Invalid action. Please try again.")
if __name__ == "__main__":
    shopping_list = []
    display_menu()