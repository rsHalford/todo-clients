#!/usr/bin/python3

import requests
from api_access import USERNAME, PASSWORD

get_about_resp = requests.get('https://todo.xhalford.com')
get_todos_resp = requests.get('https://todo.xhalford.com/api/v1/todo', auth=(USERNAME, PASSWORD))
get_about_resp_text = get_about_resp.text
print(get_about_resp_text)
get_todos_resp_json = get_todos_resp.json()
print(get_todos_resp_json)
