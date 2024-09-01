choice = "null"

tasks = []

def show_tasks():
    task_index = 0
    for task in tasks:
        print()
        print(task + " [" + str(task_index) + "]")
        task_index += 1

def add_task():
    task = input("Add task: ")
    tasks.append(task)
    print("Task added")

def delete_task():
    task_index = int(input("Input the index of the task you want to delete: "))

    if task_index < 0 or task_index > len(tasks) -1:
        print("Task with this index does not exist.")
        return
    
    tasks.pop(task_index)
    print("Task deleted")

def save_task():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task+"\n")
    


while choice != "exit":

    print("Welcome to your to-do list!")
    print("Here are your options: ")
    print("- add task (write 'add')")
    print("- delete task (write 'delete')")
    print("- show tasks (write 'show')")
    print("- save changes to txt file (write 'save')")
    print("- exit (write 'exit')")
    if choice == "show":
        show_tasks()

    if choice == "add":
        add_task()
    if choice == "delete":
        delete_task()
    if choice == "save":
        save_task()
    print()
    choice = str(input("What would you like to do? "))
print()
