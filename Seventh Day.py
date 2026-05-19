tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)

def view_task():
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        print("Your tasks:")
        for t in tasks:
            print("-", t)

def remove_task():
    task = input("Enter task to delete: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed!")
    else:
        print("Task not found!")

while True:
    print("\n1 Add task")
    print("2 View tasks")
    print("3 Remove task")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye 👋")
        break