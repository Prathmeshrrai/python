# To-Do List Application
tasks = []

def add_task():
    """Function to add a new task"""
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully.")

def view_tasks():
    """Function to view all tasks"""
    if not tasks:
        print("No tasks to display!")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{idx}. {task['task']} - {status}")
        print()

def mark_as_complete():
    """Function to mark a task as complete"""
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as complete.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    """Function to delete a task"""
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task['task']}' deleted successfully.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def menu():
    """Function to display the menu and handle user input"""
    while True:
        print("\nTo-Do List Application")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete a Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

       
