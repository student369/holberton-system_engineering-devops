#!/usr/bin/python3
"""
Extension of 0-gather_data_from_an_API.py with CSV formating.
File created: <employee_id>.csv
"""
if __name__ == "__main__":
    # Import modules
    import requests
    from sys import argv

    # Set variables
    employee_id = argv[1]
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)
    employee_url = "https://jsonplaceholder.typicode.com/users?id={}".format(
        employee_id)
    file_name = employee_id + ".csv"

    # Make requests
    todo_request = requests.get(todo_url)
    employee_request = requests.get(employee_url)

    # Get JSON results of both requests
    employee_json = employee_request.json()
    todo_json = todo_request.json()

    # Save information from requests in variables
    employee_name = employee_json[0].get('username')

    # write info into CSV file
    with open(file_name, "w") as csvfile:
        first_half = "\"" + employee_id + "\",\"" + employee_name + "\",\""
        for task in todo_json:
            if task.get("completed") is True:
                status = "True\",\""
            else:
                status = "False\",\""
            title = task.get("title") + "\""
            whole_line = first_half + status + title + "\n"
            csvfile.write(whole_line)
