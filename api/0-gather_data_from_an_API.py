#!/usr/bin/python3
"""
Script to retrieve and display information about an employee's TODO list progress.
"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Returns information about an employee's TODO list progress.
    """
    # API URLs
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Fetch user details through the API
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch user's tasks through the API
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    
    # Count completed tasks
    done_tasks = [task for task in todos_data if task['completed']]
    num_done_tasks = len(done_tasks)

    # Display TODO list progress
    print(f"Employee {employee_name} is done with tasks({num_done_tasks}/{total_tasks}):")
    
    # Print titles of completed tasks
    for task in done_tasks:
        print(f"\t{task['title']}")

if __name__ == '__main__':
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from the command-line argument
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    # Call the function to get and display TODO list progress
    get_employee_todo_progress(employee_id)
