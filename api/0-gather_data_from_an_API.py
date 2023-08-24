#!/usr/bin/python3
""" given employee ID, returns information about his/her TODO list progress."""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """ Get employee todo"""

    base_url = 'https://jsonplaceholder.typicode.com'

    user_response = requests.get(f'{base_url}/users/{employee_id}')
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data['name']
    total_tasks = len(todos_data)
    done_tasks = sum(1 for todo in todos_data if todo['completed'])

    print(f"Employee {employee_name} is done with tasks\
    ({done_tasks}/{total_tasks}):")

    for todo in todos_data:
        if todo['completed']:
            print(f"\t{todo['title']}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
