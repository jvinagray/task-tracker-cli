"""
This script provides a command-line interface for managing tasks.
It allows users to add, update, delete, list tasks, and mark tasks as in-progress or done.
"""
import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

# Ensure the tasks file exists
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return [] # Return an empty list if the file does not exist
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file) # Load tasks from the file in read mode
    except json.JSONDecodeError:
        print("Error: tasks.json is corrupted. Startin with an empty task list.")
        return []

# Save tasks to the file    
def save_tasks(tasks):
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

# Get the next available task ID
def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

# Functions to manage tasks
# Add a new task with a description, status automatically set to "todo"
def add_task(description):
    tasks = load_tasks()
    task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added succesfully: (ID: {task['id']})")

# List tasks with an optional status filter
def list_tasks(status_filter=None):
    tasks= load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    
    filtered_tasks = tasks
    if status_filter:
        filtered_tasks = [task for task in tasks if task['status'] == status_filter] # List comprehension to filter tasks by status

    for task in filtered_tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, "
        f"Created: {task['createdAt']}, Updated: {task['updatedAt']}")                                                                       

# Update a task's description by its ID
def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully. ")
            return
    print(f"Task with ID {task_id} not found.")

# Delete a task by its ID
def delete_task(task_id):
    tasks = load_tasks()
    initial_len = len(tasks)
    tasks = [task for task in tasks if task['id'] != task_id] # List comprehension to filter out the task with the given ID
    # If the length of tasks has changed, it means the task was found and deleted
    if len(tasks) < initial_len:
        save_tasks(tasks)
        print(f"Task {task_id} deleted successfully.")
    else:
        print(f"Error: Task with ID {task_id} not found.")

# Mark a task as in-progress or done by its ID
def mark_task_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}.")
            return
    print(f"Error: Task with ID {task_id} not found.")

# Command-line interface for the task management system
def main():
    if len(sys.argv) < 2: # Check if at least one command is provided
        print("Usage: python task_cli.py <command> [arguments]")
        print("Commands: add, update, delete, list, mark-in-progress, mark-done")
        return
    
    command = sys.argv[1].lower()

    # Handle different commands
    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Please provide a task description")
            return
        description = sys.argv[2]
        add_task(description)
    elif command == "list":
        status_filter = None
        if len(sys.argv) > 2:
            status_filter = sys.argv[2].lower()
            if status_filter not in ["todo", "done", "in-progress"]:
                print("Error: Invalid status filter. Use \'todo, done or in-progress\'")
                return
        list_tasks(status_filter)
    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: Please provide a task ID and a new description")
            return
        try:
            task_id = int(sys.argv[2])
            description = sys.argv[3]
            update_task(task_id, description)
        except ValueError:
            print("Error: Task ID must be an integer.")
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Please include a task ID to delete.")
            return
        try:
            task_id = int(sys.argv[2])
            delete_task(task_id)
        except ValueError:
            print("Error: Task ID must be an integer.")
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: Please include a task ID.")
            return
        try:
            task_id = int(sys.argv[2])
            mark_task_status(task_id, "in-progress")
        except ValueError:
            print("Error: Task ID must be an integer.")
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Error: Please include a task ID.")
            return
        try:
            task_id = int(sys.argv[2])
            mark_task_status(task_id, "done")
        except ValueError:
            print("Error: Task ID must be an integer.")
    else:
        print(f"Command: {command} not recognized.")

# Ensure the script can be run directly
if __name__ == "__main__":
    main()