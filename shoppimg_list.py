shopping_list = []

while True:
    action = input("\nChoose an action (add / remove / show / done): ").strip().lower()

    if action == "add":
        item = input("Enter item to add: ").strip()
        shopping_list.append(item)
        print(f"'{item}' added to the list.")

    elif action == "remove":
        item = input("Enter item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from the list.")
        else:
            print("That item is not on your list.")

    elif action == "show":
        if not shopping_list:
            print("Your list is empty.")
        else:
            print("Your Shopping List:")
            for item in shopping_list:
                print(item)

    elif action == "done":
        print("Goodbye!")
        break

    else:
        print("Invalid action. Please choose add, remove, show, or done.")
