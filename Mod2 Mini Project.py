#mini project - To-Do List Application


to_do_list = []
completed_tasks = []

def add_task(task):
    global to_do_list
    if task.strip():
        to_do_list.append(task)
    else: 
        print("Error! Please enter a task, we cannot leave it empty!")

def view_task():
    global to_do_list
    global completed_tasks
    print(f"Your to-do list is as follows: {to_do_list}")
    print(f"Your completed list is as follows: {completed_tasks}")

def task_complete(task):
    global to_do_list
    global completed_tasks
    if task in to_do_list:
        to_do_list.remove(task)
        completed_tasks.append(task)
        print(f"Your completed tasks are as follows: {completed_tasks}")
    else:
        print(f" Error! Your task: '{task}' is not included in the below lists, please see below: ")
        print(f" To do list: {to_do_list}")
        print(f" Completed tasks: {completed_tasks} ")

def delete_task(task):
    global to_do_list
    global completed_tasks
    if task in to_do_list:
        to_do_list.remove(task)
        print(f"Your task: {task} has been deleted from the to do list.")
    elif task in completed_tasks:
        completed_tasks.remove(task)
        print(f"Task '{task}' has been deleted from Completed list")
    else:
        print(f" Error! Your task: '{task}' is not included in the below lists, please select from the below tasks:")
        print(f" To do list: {to_do_list}")
        print(f" Completed tasks: {completed_tasks} ")

while True:
    action = input(""" 
                   Welcome to the To-Do List App!

    Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit               
    Please type '1', '2', '3', '4', or '5' based on the above options \n
                   """)
    try:
        if action == '1':
            task = input("Please type a task to add to your to-do list:  \n").lower()
            add_task(task)

        elif action == '2':
            view_task()
        elif action == '3':
            task = input("Please type a task to add to your completed list:  ").lower()
            task_complete(task)
        elif action == '4':
            task = input("Please type a task to remove from your list:  ").lower()
            delete_task(task)
        elif action == '5':
            print("Exiting the To-Do List Application. Thank you for visiting!")
            break
        else:
            print("Invalid option. Please choose again.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
