#!/usr/bin/python3
""" given employee ID, returns information about his/her TODO list progress."""

import json
import requests


def get_employee_todo_progress(employee, base_url):
    """ Get employee todo"""

    todos_response = requests.get(f'{base_url}/todos?userId={employee["id"]}')

    todos_data = todos_response.json()

    employee_name = employee['username']

    lis_data = []
    for todo in todos_data:
        dic_data = {"username": employee_name,
                    "task": todo["title"],
                    "completed": todo["completed"]}
        lis_data.append(dic_data)

    return lis_data


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com'
    user_response = requests.get(f'{base_url}/users/')
    user_data = user_response.json()

    dic = {}
    for employee in user_data:
        key = f"{employee['id']}"
        dic[key] = get_employee_todo_progress(employee, base_url)

    with open("todo_all_employees.json", 'w') as f:
        json.dump(dic, f)
