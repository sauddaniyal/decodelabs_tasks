# *==========MENU Function============*

def menu():
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View task_list")
    print("3. Delete Task")
    print("4. Exit")
    print("================================")

task_list = []

# *======While Loop============*

while True:
    menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter your task: ").strip()
        task_list.append(task)
        print("Task added successfully!")

    elif choice == 2:
        if len(task_list) == 0:
            print("No task_list available.")
        else:
            print("\nYour task_list:")
            for i, task in enumerate(task_list, start=1):
                print(i, ".", task)

    elif choice == 3:
        if len(task_list) == 0:
            print("No task_list to delete.")
        else:
            print("\nYour task_list:")
            for i, task in enumerate(task_list, start=1):
                print(i, ".", task)
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(task_list):
                removed_task = task_list.pop(task_no - 1)
                print(removed_task, "deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == 4:
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please select between 1 and 4.")

