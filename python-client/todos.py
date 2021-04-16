#/usr/bin/python3

import argparse
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
    title_valid = False
    body_valid = False
    while not title_valid:
        title = input('Title: ')
        if len(title) <= 10:
            title_valid = True
        else:    
            print('Error! Title can\'t be longer than 10 characters.')
    while not body_valid:
        body = input('Body: ')
        if len(body) <= 100:
            body_valid = True
        else:
            print('Error! Body must only be 100 characters long.')
    data = {'title': title, 'body': body}
    resp = requests.post(url + '/api/v1/todo', auth=auth, json=data)
    print(resp.json())

def get_all_todos():
    resp = requests.get(url + '/api/v1/todo', auth=auth)
    data = resp.json()
    print(data)

def get_todo_by_id():
    id = input('Select todo: ')
    resp = requests.get(url + '/api/v1/todo/' + id, auth=auth)
    data = resp.json()
    print(data)

def update_todo_by_id():
    id = input('Select which todo to update: ')
    print('Enter your todo\'s details.')
    title_valid = False
    body_valid = False
    while not title_valid:
        title = input('Title: ')
        if len(title) <= 10:
            title_valid = True
        else:    
            print('Error! Title can\'t be longer than 10 characters.')
    while not body_valid:
        body = input('Body: ')
        if len(body) <= 100:
            body_valid = True
        else:
            print('Error! Body must only be 100 characters long.')
    data = {'title': title, 'body': body}
    resp = requests.put(url + '/api/v1/todo/' + id, auth=auth, json=data)
    print(resp.json())

def delete_todo_by_id():
    id = input('Select which todo to delete: ')
    resp = requests.delete(url + '/api/v1/todo/' + id, auth=auth)

parser = argparse.ArgumentParser()
parser.add_argument('list', help='List all todos.')
parser.add_argument('add', help='Add a new todo.')
parser.add_argument('update', help='Update a todo.')
parser.add_argument('delete', help='Delete a todo.')
args = parser.parse_args()

