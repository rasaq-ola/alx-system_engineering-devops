#!/usr/bin/python3
import json
import requests

def export_all_to_json():
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

    data = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_tasks = [{"username": username, "task": task.get('title'), "completed": task.get('completed')} for task in todos if task.get('userId') == user_id]
        data[user_id] = user_tasks

    filename = "todo_all_employees.json"
    with open(filename, mode='w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    export_all_to_json()
