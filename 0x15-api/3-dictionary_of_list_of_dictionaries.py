#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users_data = users_response.json()
    todos_data = todos_response.json()

    user_dict = {}
    for user in users_data:
        user_id = user["id"]
        user_dict[user_id] = []

    for todo in todos_data:
        task = {"username": "", "task": "", "completed": ""}
        task["task"] = todo["title"]
        task["completed"] = todo["completed"]

        user_id = todo["userId"]
        task["username"] = next(
            user["username"] for user in users_data if user["id"] == user_id
        )

        user_dict[user_id].append(task)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(user_dict, json_file)
