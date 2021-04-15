#/usr/bin/python3

import requests
from api_access import USERNAME, PASSWORD

url = 'https://todo.xhalford.com'
auth = (USERNAME, PASSWORD)

def get_about():
    resp = requests.get(url)
    text = resp.text
    print(text)

def create_todo():
    print('Enter your todo\'s details.')
    title = input('Title: ')
    if len(title) > 10:
        print('Error! Title must only be 10 characters long.')
        return create_todo()
    body = input('Body: ')
    if len(body) > 100:
        print('Error! Body must only be 100 characters long.')
        return create_todo()
    data = {'title': title, 'body': body}
    resp = requests.post(url + '/api/v1/todo', auth=auth, json=data)
    print(resp.json())

def get_all_todos():
    resp = requests.get(url + '/api/v1/todo', auth=auth)
    data = resp.json()
    print(data)

def get_todo_by_id(id):
    id = str(id)
    resp = requests.get(url + '/api/v1/todo/' + id, auth=auth)
    data = resp.json()
    print(data)

def update_todo_by_id():
    id = input('Select which todo to update: ')
    print('Enter your todo\'s details.')
    title = input('Title: ')
    if len(title) > 10:
        print('Error! Title must only be 10 characters long.')
        return create_todo()
    body = input('Body: ')
    if len(body) > 100:
        print('Error! Body must only be 100 characters long.')
        return create_todo()
    data = {'title': title, 'body': body}
    resp = requests.put(url + '/api/v1/todo/' + id, auth=auth, json=data)
    print(resp.json())

def delete_todo_by_id(id):
    id = str(id)
    resp = requests.delete(url + '/api/v1/todo/' + id, auth=auth)
