shopping_list = []
def shopping_list_manager():
    while True:
        action = input("Enter 'add' to add an item, 'remove' to remove an item, 'view' to view the list, or 'exit' to quit: ").strip().lower()
        if action == 'add':
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")
        elif action == 'remove':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in your shopping list.")
        elif action == 'view':
            if shopping_list:
                print("Your shopping list:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is empty.")
        elif action == 'exit':
            print("Exiting the shopping list manager. Goodbye!")
            break

        else:
            print("Invalid action. Please try again.")
if __name__ == "__main__":
    shopping_list_manager()