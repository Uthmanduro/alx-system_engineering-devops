#!/usr/bin/python3
"""A python script that export data in csv format"""
import csv
import requests
import csv


if __name__ == "__main__":
    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        exit()
    user_todo = requests.get('https://jsonplaceholder.typicode.com/todos{}={}'.
                             format("?userId", emp_id))
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(emp_id))

    filename = "{}.csv".format(emp_id)

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=",", quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for records in user_todo.json():
            fmt = [emp_id, user.json().get("username"),
                   records.get("completed"), records.get("title")]
            writer.writerow(fmt)
