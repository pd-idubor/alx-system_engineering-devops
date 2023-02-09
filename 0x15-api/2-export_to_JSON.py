#!/usr/bin/python3
"""Gathering API data"""
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    user = requests.get(url)
    name = user.json().get("username")

    url = "https://jsonplaceholder.typicode.com/todos"
    todo = requests.get(url, params={"userId": id}).json()

    t_list = []
    file_name = "{}.json".format(id)

    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = name
        t_list.append(task_dict)

    data = {"{}".format(id): t_list}
    with open(file_name, "a") as fd:
        json.dump(data, fd)
