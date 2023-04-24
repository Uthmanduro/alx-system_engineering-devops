#!/usr/bin/python3
"""script the uses REST API to return info about an employee TODO list"""
import sys
import requests


if __name__ == '__main__':
    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        exit()
    user_todo = requests.get('https://jsonplaceholder.typicode.com/todos{}={}'.format("?userId", emp_id))
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(emp_id))
    
    task_length = []
    count = []
    for todos in user_todo.json():
        if todos.get("completed") == True:
            count.append(todos.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(users.json().get("name"),
          len(count), len(user_todo.json())))
    [print("\t" + title) for title in count]
