#!/usr/bin/python3
import json
import requests
import sys

def export_to_json(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user = user_response.json()
    todos = todos_response.json()

    username = user.get('username')

    tasks = [{"task": task.get('title'), "completed": task.get('completed'), "username": username} for task in todos]

    data = {employee_id: tasks}
    filename = f"{employee_id}.json"
    with open(filename, mode='w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
