import requests
import sys

def get_employee_todo_progress(employee_id):
    # Get user details through the API
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    user_data = user_response.json()
    employee_name = user_data['name']

    # Get user's tasks through the API
    todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todo_data = todo_response.json()
    total_tasks = len(todo_data)

    # Get the number of completed tasks
    done_tasks = [task for task in todo_data if task['completed']]
    num_done_tasks = len(done_tasks)

    # Display TODO list progress
    print(f"Employee {employee_name} is done with tasks({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

