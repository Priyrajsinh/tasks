# create an empty list to store the tasks and their status
todo_list = []

#Function to add a task
def add_task():
    task = input("ENter a task: ")
    todo_list.append({"Task": task, "Status": "pending"})
    print("New task added successfully!\n")

#Function to view all task
def view_task():
    print("Your To-Do list")
    if len(todo_list) == 0:
        print("No pending tasks")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}: {task['Task']} - {task['Status']}")
    print("\n")

#Function to remove a Task:
def remove_task():
    if len(todo_list) == 0:
        print("List is empty")
    else:
        try:
            search_index = int(input("Enter the task number that you want to remove:")) - 1
            if 0 <= search_index <= len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task Removed: {removed_task['Task']}")
            else:
                print("Invalid Task Number")
        except ValueError:
            print("Please enter a valid task number")

#Funtion to mark a task as done
def mark_done():
    if len(todo_list) == 0:
        print("List is empty")
    else:
        try:
            search_index = int(input("Enter the task number that you want to mark as complete:")) - 1
            if 0 <= search_index <= len(todo_list):
                todo_list[search_index]["Status"] = "done"
                print(f"Task {todo_list[search_index]['Task']} has benn marked as Done")
            else:
                print("Invalid Task Number")
        except ValueError:
            print("Please enter a valid task number")

# Function to display a menu
def menu():
    while(True):
        print("****Main Menu****")
        print("1. Add a new task: ")
        print("2. View all task: ")
        print("3. Remove a task: ")
        print("4. Mark a task as completed: ")
        print("5. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Exciting the application! Thanks for using the To Do list")
            quit()
        else:
            print("Invalid choice try again")
        
menu()