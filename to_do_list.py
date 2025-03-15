import json

# File to store tasks
task_file = "tasks.json"

def load_tasks():
    """Load tasks from a file."""
    try:
        with open(task_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(task_file, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added successfully!")

def remove_task(task):
    """Remove a task."""
    tasks = load_tasks()
    if task in tasks:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task '{task}' removed successfully!")
    else:
        print("Task not found.")

def view_tasks():
    """View all tasks."""
    tasks = load_tasks()
    if tasks:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    else:
        print("\nNo tasks found!")

def main():
    """Main function to run the to-do list app."""
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter task to remove: ")
            remove_task(task)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
