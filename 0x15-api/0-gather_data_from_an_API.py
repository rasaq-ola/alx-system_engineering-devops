#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    tasks_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    )

    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()
    completed_tasks = [
        task for task in tasks_data if task.get("completed")
    ]

    print(f"Employee {employee_name} is done with tasks "
          f"({len(completed_tasks)}/{len(tasks_data)}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
