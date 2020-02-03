#!/usr/bin/python3
"""
Python script to get some API information.
"""
if __name__ == "__main__":

    # Import modules
    import requests
    import sys

    # Set variables
    employee_id = sys.argv[1]
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    employee_url = "https://jsonplaceholder.typicode.com/users"

    # Set payloads
    todo_payload = {'userId': employee_id}
    employee_payload = {'id': employee_id}

    # Make requests
    todo_request = requests.get(todo_url, params=todo_payload)
    employee_request = requests.get(employee_url, params=employee_payload)

    # Get JSON results of both requests
    employee_json = employee_request.json()
    todo_json = todo_request.json()

    # Save information from requests in variables
    employee_name = employee_json[0].get('name')
    total_tasks = len(todo_json)

    ##
    # Go through the tasks
    #     If task is complete, add to the completed_tasks list and
    #     update the completed_counter
    ##
    completed_counter = 0
    completed_tasks = []
    for task in todo_json:
        if task.get('completed') is True:
            completed_counter += 1
            completed_tasks.append(task.get('title'))

    # Print in correct format
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_counter, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))
