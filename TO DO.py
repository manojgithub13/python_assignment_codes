tasks = []

while True:
    print("To do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter the task you want to add: ")
        tasks.append(task)
        print(f"Task '{task}' has been added.")
    elif choice == "2":
        abc = input("Enter the task you want to remove: ")
        if abc in tasks:
            tasks.remove(task)
            print(f"Task '{task}' has been removed.")
        else:
            print(f"Task '{task}' not found in the list.")
    elif choice == "3":
        if not tasks:
            print("No tasks in the list.")
        else:
            print("Tasks in the list:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4).")


