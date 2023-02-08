#!/usr/bin/python3
"""Gathering API data"""
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    user = requests.get(url)
    name = user.json().get("name")

    url = "https://jsonplaceholder.typicode.com/todos/"
    todo = requests.get(url, params={"userId": id}).json()

    t_complete = 0
    t_list = ""

    for task in todo:
        if (task.get("completed") is True):
            t_complete += 1
            t_list += "\t " + task.get("title") + "\n"

    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          t_complete,
                                                          len(todo)))

    print(t_list[:-1])
