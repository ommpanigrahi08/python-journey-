tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)

def view_task():
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        for i in range(len(tasks)):
             print(i + 1, tasks[i])

def remove_task():
    task_number = int(input("Enter task number to delete: "))

    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task removed!")
    else:
        print("Invalid task number!")

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
        print("Goodbye. See you next time !")
        break