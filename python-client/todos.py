#/usr/bin/python3

import sys
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


class TodoParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

parser = TodoParser(prog='Todos', description='List, add, update and delete your todo list from the command-line.', epilog='Thanks for choosing to use Todos!')
parser.version = '1.0.0'
exclusive = parser.add_mutually_exclusive_group()
exclusive.add_argument('-a', '--add', action='store_true', help='add a new todo')
exclusive.add_argument('-d', '--delete', action='store_true', help='delete a selected todo')
exclusive.add_argument('-l', '--list', action='store_true', help='list all todos')
exclusive.add_argument('-s', '--select', action='store_true', help='list all todos')
exclusive.add_argument('-u', '--update', action='store_true', help='update a selected todo entry')
parser.add_argument('-v', '--version', action='version')
args = parser.parse_args()

if args.add:
    create_todo()
elif args.delete:
    delete_todo_by_id()
elif args.list:
    get_all_todos()
elif args.select:
    get_todo_by_id()
elif args.update:
    update_todo_by_id()
else:
    print(parser.print_help())
