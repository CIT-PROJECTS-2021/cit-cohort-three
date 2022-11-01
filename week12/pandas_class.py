import pandas as pd
import requests


data_set = {
    'name': ['John', 'Jane', 'Joe', 'Jack', 'Jill'],
    'marks': [90, 80, 70, 60, 50],
}

df = pd.DataFrame(data_set)

print(df)

# panda series
arr = [i+1 for i in range(10)]

ps = pd.Series(arr)

print(ps[0])

# print(ps)

# Labels
ps = pd.Series(arr, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

# print(ps)

print(ps['a'])

calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390,
    "day4": 420,
}


p_calories = pd.Series(calories)
print(p_calories)

# Locate a row

df = pd.DataFrame(calories, index=['day1', 'day2', 'day3', 'day4'])
print(df.loc['day2'])

# Load CSV
def download_csv(url):
    r = requests.get(url)
    with open('data.csv', 'wb') as f:
        f.write(r.content)

import os

if not os.path.exists('data.csv'):
    download_csv('https://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv')


df = pd.read_csv('data.csv')
print(df)

df = pd.read_csv('bands.csv')
print(df.head())

# Read JSON data

todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

df = pd.DataFrame(todos)

print(df.head())