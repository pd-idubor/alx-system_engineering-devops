#!/usr/bin/python3
"""Gathering API data"""
import json
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/users"
    user = requests.get(url)

    url = "https://jsonplaceholder.typicode.com/todos"

    t_list = []
    file_name = "todo_all_employees.json"

    for u in user.json():
        id = u.get("id")
        todo = requests.get(url, params={"userId": id}).json()
        name = u.get("username")
        for task in todo:
            task_dict = {}
            task_dict["username"] = name
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            t_list.append(task_dict)

        data = {"{}".format(id): t_list}
        with open(file_name, "a") as fd:
            json.dump(data, fd)
