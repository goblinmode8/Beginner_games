# LIST MANAGEMENT APP

# basically turning Python data into something that can be saved
# json module provides straightforward tools to read (load) and write (dump)
# JSON data using standard Python file operations.

import json

file_name = "todo_list.json"

# Load existing items
    # If no saved data exists, start with an empty list
def load_tasks():
    try:
        with open(file_name,"r") as file:
            return json.load(file)  # give python dictionary version of the file
    except:
        return {"tasks": []}


def save_tasks(tasks):
    # w == override mode, delete and recreate list
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file)  # dump == dump tasks into file
    except:
        return {"Failed  to save tasks" : []}


def view_tasks(tasks):
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks available!")
    else:
        print("\nYour To-Do List: ")

        task_number = 1

        for idx, task in enumerate(task_list):
            # look to see if tasks is True (completed)
            if not task["deleted"]:
                status = task["complete"] if task["complete"] else "Pending"
                print(f"{task_number}. {task['description']} | {status}")
                task_number += 1


# can modify dictionary and any changes made will exist outside
def create_tasks(tasks):
    description = input("Enter tasks description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False, "deleted": False})
        save_tasks(tasks)
        print("Task created successfully!")
    else:
        print("Description cannot be empty!")


# Let user select an item and mark item as complete
def mark_task_complete(tasks):
    try:
        view_tasks(tasks)
        task_number = int(input("Enter task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            # need to -1 bc index starts at 0
            tasks["tasks"][task_number - 1]["complete"] = True
            save_tasks(tasks)
            print("Task marked successfully!")
        else:
            print("Task number out of range!")
    except:
        print("Enter a valid task number!")


def delete_tasks(tasks):
    try:
        view_tasks(tasks)
        task_number = int(input("Enter task number to delete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            # need to -1 bc index starts at 0
            tasks["tasks"][task_number - 1]["deleted"] = True
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Task number out of range!")
    except ValueError:
        print("Enter a valid task number!")


def main():
    # save_tasks({"tasks": "saved tasks"})
    tasks = load_tasks()
    print(tasks)

    # Display menu / operations
    while True:
        print("\n To-Do List Manager :)")
        print("1. View Task")
        print("2. Create Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_tasks(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Please enter a valid choice!")

main()
