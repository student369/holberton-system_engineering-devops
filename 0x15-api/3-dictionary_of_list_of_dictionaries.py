#!/usr/bin/python3
"""
Extension of the 0-gather_data_from_an_API.py with JSON formating.
File createded: todo_all_employees.json
"""
if __name__ == "__main__":

    # Import modules
    import json
    import requests

    # Set variables
    employee_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    file_name = "todo_all_employees.json"

    # Make requests
    employee_response = requests.get(employee_url).json()
    todo_response = requests.get(todo_url).json()

    full_todo = {}  # Empty dictionary for all employees and todo lists

    with open(file_name, "w") as json_file:  # Open file_name
        for employee in employee_response:  # Create indv employee todo list
            employee_tasks = []
            for task in todo_response:  # Create indv tasks
                task_dict = {}
                if task.get("userId") == employee.get("id"):
                    task_dict["username"] = employee.get("username")
                    task_dict["task"] = task.get("title")
                    task_dict["completed"] = task.get("completed")
                    employee_tasks.append(task_dict)
            full_todo[employee.get("id")] = employee_tasks  # Add employee todo
        json.dump(full_todo, json_file)  # write to file
