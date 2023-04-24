#!/usr/bin/python3
"""script that exports data in json format"""
import json
import requests
import sys

if __name__ == "__main__":
    try:
        emp_id = sys.argv[1]
    except ValueError:
        exit()

    user_todo = requests.get('https://jsonplaceholder.typicode.com/todos{}={}'.
                             format("?userId", emp_id))
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(emp_id))

    filename = "{}.json".format(emp_id)
    employee = {}
    employee_list = []
    for todos in user_todo.json():
        inner_dict = {}
        inner_dict["task"] = todos.get("title")
        inner_dict["completed"] = todos.get("completed")
        inner_dict["username"] = user.json().get("username")
        employee_list.append(inner_dict)
    employee[str(emp_id)] = employee_list
    with open(filename, 'w') as f:
        json.dump(employee, f)
