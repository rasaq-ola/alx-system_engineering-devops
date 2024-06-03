#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    todos_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    )

    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    completed_tasks = [
        task for task in todos_data if task.get("completed")
    ]
    completed_task_titles = [
        task.get("title") for task in completed_tasks
    ]
    total_tasks = len(todos_data)
    completed_tasks_count = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with tasks("
        f"{completed_tasks_count}/{total_tasks}):"
    )
    for title in completed_task_titles:
        print(f"\t {title}")
