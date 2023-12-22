#!/usr/bin/python3

import requests
import sys

def get_employee_todo_progress(employee_id):
    user_response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    user_data = user_response.json()
    employee_name = user_data['name']

    todo_response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            employee_id))
    todo_data = todo_response.json()
    total_tasks = len(todo_data)

    done_tasks = [task for task in todo_data if task['completed'] is True]
    num_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_done_tasks, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task['title']))

if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
