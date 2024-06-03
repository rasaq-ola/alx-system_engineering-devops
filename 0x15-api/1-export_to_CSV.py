#!/usr/bin/python3
"""
Script to fetch TODO list progress for a given employee ID and export to CSV
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data.get('username')

    with open('{}.csv'.format(employee_id), mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, username, task.get('completed'), task.get('title')])
