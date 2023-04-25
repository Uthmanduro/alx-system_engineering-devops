#!/usr/bin/python3
"""A script that export data in json format"""
import json
import requests
import sys


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users")
    all_employee = {}
    for users in user.json():
        employee_data = []
        url = "https://jsonplaceholder.typicode.com/todos?userId={}".\
              format(users.get("id"))
        employee = requests.get(url)
        for employees in employee.json():
            inner_dict = {}
            inner_dict["username"] = users.get("username")
            inner_dict["task"] = employees.get("title")
            inner_dict["completed"] = employees.get("completed")
            employee_data.append(inner_dict)
        all_employee[users.get("id")] = employee_data

    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_employee, f)
