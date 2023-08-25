#!/usr/bin/python3
""" given employee ID, returns information about his/her TODO list progress."""

import requests
import csv
import sys


def get_employee_todo_progress(employee_id):
    """ Get employee todo"""

    base_url = 'https://jsonplaceholder.typicode.com'

    user_response = requests.get(f'{base_url}/users/{employee_id}')
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data['username']
    total_tasks = len(todos_data)
    done_tasks = sum(1 for todo in todos_data if todo['completed'])

    csv_filename = f'{employee_id}.csv'

    with open(csv_filename, 'w', newline='') as f:
        for todo in todos_data:
            f.write(f'"{todo["userId"]}","{employee_name}",\
"{todo["completed"]}","{todo["title"]}"\n')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
