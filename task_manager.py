"""
Simple CLI Task Manager
A beginner-friendly command-line tool to manage tasks stored in a JSON file.
"""

import json
import os
import sys
from datetime import datetime

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file. Return empty list if file doesn't exist."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    """Save the tasks list to the JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(description):
    """Add a new task to the list."""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "done": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Added task #{task['id']}: {description}")


def list_tasks():
    """Print all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet. Use 'add <description>' to create one.")
        return
    print("\nYour tasks:")
    print("-" * 50)
    for task in tasks:
        status = "✔" if task["done"] else "○"
        print(f"[{status}] #{task['id']}  {task['description']}  ({task['created_at']})")
    print("-" * 50)


def complete_task(task_id):
    """Mark a task as done."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"✅ Completed task #{task_id}")
            return
    print(f"❌ Task #{task_id} not found")


def delete_task(task_id):
    """Delete a task by ID."""
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"❌ Task #{task_id} not found")
        return
    save_tasks(new_tasks)
    print(f"🗑️ Deleted task #{task_id}")


def print_help():
    print("""
Usage:
  python task_manager.py add "Buy milk"
  python task_manager.py list
  python task_manager.py complete 1
  python task_manager.py delete 1
""")


def main():
    """Entry point: parse command-line arguments."""
    args = sys.argv[1:]

    if not args:
        print_help()
        return

    command = args[0].lower()

    if command == "add":
        if len(args) < 2:
            print("❌ Please provide a task description")
            return
        add_task(" ".join(args[1:]))
    elif command == "list":
        list_tasks()
    elif command == "complete":
        if len(args) < 2:
            print("❌ Please provide a task ID")
            return
        complete_task(int(args[1]))
    elif command == "delete":
        if len(args) < 2:
            print("❌ Please provide a task ID")
            return
        delete_task(int(args[1]))
    elif command in ("help", "-h", "--help"):
        print_help()
    else:
        print(f"❌ Unknown command: {command}")
        print_help()


if __name__ == "__main__":
    main()