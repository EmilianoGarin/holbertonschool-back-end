#!/usr/bin/python3
""" given employee ID, returns information about his/her TODO list progress."""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """ Get employee todo"""

    base_url = 'https://jsonplaceholder.typicode.com'

    user_response = requests.get(f'{base_url}/users/{employee_id}')
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data['username']

    lis_data = []
    for todo in todos_data:
        dic_data = {"task": todo["title"],
                    "completed": todo["completed"],
                    "username": employee_name}
        lis_data.append(dic_data)

    json_filename = f'{employee_id}.json'
    with open(json_filename, 'w') as f:
        json.dump({f"{employee_id}": lis_data}, f)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
