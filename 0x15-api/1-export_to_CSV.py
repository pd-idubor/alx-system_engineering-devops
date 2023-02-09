#!/usr/bin/python3
"""Gathering API data"""
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    user = requests.get(url)
    name = user.json().get("username")

    url = "https://jsonplaceholder.typicode.com/todos"
    todo = requests.get(url, params={"userId": id}).json()

    data = ""
    file_name = "{}.csv".format(id)

    with open(file_name, "a") as fd:
        for task in todo:
            status = task.get("completed")
            title = task.get("title")
            data = "\"{}\", \"{}\", \"{}\", \"{}\"\n".format(id,
                                                             name,
                                                             status,
                                                             title)
            fd.write(data)
