tasks = []


def addTask():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the List")


def deleteTask():
    listTask()
    try:
        taskToDelete = int(input("Enter the # of the task to delete: "))
        if 0 <= taskToDelete <= len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task #{taskToDelete} is removed.")
        else:
            print(f"Task '#{taskToDelete}' not found.")
    except:
        print("Invalid input.")


def listTask():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current tasks:")
        for index , task in enumerate(tasks):
            print(f"Task #{index}. '{task}'")
            index += 1


if __name__ == "__main__":
    print("Welcome to My ToDoList App :)")
    while True:
        print("\n")
        print("Please select one option from the below")
        print("-------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List of tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTask()
        elif choice == "4":
            break
        else:
            print("Invalid input Please try again!!")

    print("Goodbye!!!\nGood to see you next time!")