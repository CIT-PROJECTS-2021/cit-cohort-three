# Todo commandline application using argparse and sys.argv
# This app will use a dictionary to store the todo list

import argparse
import sys
import os
import datetime
import time
import json
import pickle


def get_parser():
    parser = argparse.ArgumentParser(description='Todo application')
    parser.add_argument('-a', '--add', help='Add a new task', action='store_true')
    parser.add_argument('-l', '--list', help='List all tasks', action='store_true')
    parser.add_argument('-r', '--remove', help='Remove a task', action='store_true')
    parser.add_argument('-c', '--complete', help='Complete a task', action='store_true')
    parser.add_argument('-d', '--delete', help='Delete a task', action='store_true')
    parser.add_argument('-s', '--show', help='Show a task', action='store_true')
    return parser


def add_task(todo_list):
    task = input('Enter task: ')
    todo_list.append(task)
    print('Task added')


def list_tasks(todo_list):
    print('\nTodo list:')
    for i, task in enumerate(todo_list):
        print(f'{i + 1}. {task}')


def remove_task(todo_list):
    list_tasks(todo_list)
    task_number = int(input('Enter task number to remove: '))
    todo_list.pop(task_number - 1)
    print('Task removed')


def complete_task(todo_list):
    list_tasks(todo_list)
    task_number = int(input('Enter task number to complete: '))
    todo_list[task_number - 1] = '✔ ' + todo_list[task_number - 1]
    print('Task completed')


def delete_task(todo_list):
    list_tasks(todo_list)
    task_number = int(input('Enter task number to delete: '))
    todo_list.pop(task_number - 1)
    print('Task deleted')


def show_task(todo_list):
    list_tasks(todo_list)
    task_number = int(input('Enter task number to show: '))
    print(todo_list[task_number - 1])


def main():
    parser = get_parser()
    args = parser.parse_args()
    todo_list = []
    if os.path.exists('todo.json'):
        with open('todo.json', 'r') as f:
            todo_list = json.load(f)
    elif os.path.exists('todo.pickle'):
        with open('todo.pickle', 'rb') as f:
            todo_list = pickle.load(f)
    if args.add:
        add_task(todo_list)
    elif args.list:
        list_tasks(todo_list)
    elif args.remove:
        remove_task(todo_list)
    elif args.complete:
        complete_task(todo_list)
    elif args.delete:
        delete_task(todo_list)
    elif args.show:
        show_task(todo_list)
    else:
        print('No arguments given')
        # show usage
        parser.print_help()
    with open('todo.json', 'w') as f:
        json.dump(todo_list, f)
    with open('todo.pickle', 'wb') as f:
        pickle.dump(todo_list, f)


if __name__ == '__main__':
    main()

