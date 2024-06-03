#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import csv
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
    employee_username = user_data.get("username")

    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()

    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in tasks_data:
            csv_writer.writerow([employee_id, employee_username,
                                 task.get("completed"), task.get("title")])
