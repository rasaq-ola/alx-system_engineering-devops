#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
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
    username = user_data.get("username")

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos_data
    ]

    json_data = {employee_id: tasks}

    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(json_data, json_file)
