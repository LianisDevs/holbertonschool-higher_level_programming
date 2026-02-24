#!/usr/bin/python3

"""
This is the task_02_requests module
Contains fetch_and_print_posts() and fetch_and_save_posts()
"""

import requests
import csv


def fetch_and_print_posts():
    posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(posts.status_code))
    print(posts.headers)

    if posts.status_code == 200:
        posts_obj = posts.json()
        for i in posts_obj:
            print(i["title"])


def fetch_and_save_posts():
    posts = requests.get('https://jsonplaceholder.typicode.com/posts')

    if posts.status_code == 200:
        posts_obj = posts.json()
        if posts_obj:
            fieldnames = posts_obj[0].keys()
        else:
            fieldnames = []
        try:
            with open("posts.csv", "w", newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(posts_obj)
        except Exception:
            pass
