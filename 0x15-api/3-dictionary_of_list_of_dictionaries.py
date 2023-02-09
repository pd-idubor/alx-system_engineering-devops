#!/usr/bin/python3
"""Gathering API data"""
import json
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/users"
    user = requests.get(url)

    file_name = "todo_all_employees.json"

    for u in user.json():
        t_list = []
        id = u.get("id")
        url = "https://jsonplaceholder.typicode.com/todos"
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
