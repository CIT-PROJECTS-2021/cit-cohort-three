# 1. Weather Program Python Project
#    Using the requests library, create a 
# program that will take a city name as input 
# and return the current weather for that city. 
# The program should also save the city name and 
# the current weather to a file. The program should 
# also be able to read the file and print the city 
# name and the current weather. 
# Use this API to get the weather data: https://openweathermap.org/current

# 2. Password Generator Python Project
#    Create a program that generates 
# a random password for the user. 
# Ask the user how long they want their password to be, 
# and how many letters and numbers they want in their password. 
# Have a mix of upper and lowercase letters, as well as numbers and symbols.
#  The password should be a minimum of 6 characters long.

# 3. Interactive  quiz Python Project
#    Create a program that asks the user a series of questions. 
# Each question should have a multiple choice answer. 
# The user should be able to type in the letter of the answer they think is correct.
#  After all the questions have been asked, the program should tell the user how many 
# they got correct and what the correct answers were.

# 4. Country Cities Guessing Game Python Project
#    Create a program that will ask a user to guess the capital of a country. 
# The program should have a list of at least 10 countries and their capitals. 
# The program should randomly choose a country and ask the user to guess the capital. 
# The program should tell the user if they are correct or not. 
# The program should also keep track of how many questions the user gets correct and print that out at the end. 
# Use this link to programatically get the list of countries and their capitals: https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-capital-city.json

# 1. Weather Program Python Project
import requests
import json

def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=9d4c4d4e4b4f4b4c4e4f4d4f4c4e4f4c".format(city)
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def print_weather(data):
    print("The weather in {} is {}.".format(data["name"], data["weather"][0]["description"]))
    print("The temperature is {} degrees Fahrenheit.".format(data["main"]["temp"] * 9/5 - 459.67))
    print("The humidity is {}%.".format(data["main"]["humidity"]))
    print("The wind speed is {} mph.".format(data["wind"]["speed"]))
    print("The pressure is {} hPa.".format(data["main"]["pressure"]))
    print("The cloudiness is {}%.".format(data["clouds"]["all"]))
    print("The sunrise is at {}.".format(data["sys"]["sunrise"]))
    print("The sunset is at {}.".format(data["sys"]["sunset"]))
    print("The geo coords are [{}, {}].".format(data["coord"]["lon"], data["coord"]["lat"]))
    print("The country is {}.".format(data["sys"]["country"]))
    print("The timezone is {}.".format(data["timezone"]))
    
def save_weather(data):
    with open("weather.txt", "w") as file:
        file.write("The weather in {} is {}.".format(data["name"], data["weather"][0]["description"]))
        file.write("The temperature is {} degrees Fahrenheit.".format(data["main"]["temp"] * 9/5 - 459.67))
        file.write("The humidity is {}%.".format(data["main"]["humidity"]))
        file.write("The wind speed is {} mph.".format(data["wind"]["speed"]))
        file.write("The pressure is {} hPa.".format(data["main"]["pressure"]))
        file.write("The cloudiness is {}%.".format(data["clouds"]["all"]))
        file.write("The sunrise is at {}.".format(data["sys"]["sunrise"]))
        file.write("The sunset is at {}.".format(data["sys"]["sunset"]))
        file.write("The geo coords are [{}, {}].".format(data["coord"]["lon"], data["coord"]["lat"]))
        file.write("The country is {}.".format(data["sys"]["country"]))
        file.write("The timezone is {}.".format(data["timezone"]))

# 2. Password Generator Python Project
import random
import string

def get_password():
    length = int(input("How long do you want your password to be? "))
    letters = int(input("How many letters do you want in your password? "))
    numbers = int(input("How many numbers do you want in your password? "))
    symbols = int(input("How many symbols do you want in your password? "))
    password = ""
    for i in range(letters):
        password += random.choice(string.ascii_letters)
    for i in range(numbers):
        password += random.choice(string.digits)
    for i in range(symbols):
        password += random.choice(string.punctuation)
    password = list(password)
    random.shuffle(password)
    password = "".join(password)
    return password

# 3. Interactive  quiz Python Project
import random

def get_questions():
    questions = []
    with open("questions.txt", "r") as file:
        for line in file:
            questions.append(line.strip().split(","))
    return questions

def get_answers(questions):
    answers = []
    for question in questions:
        print(question[0])
        for i in range(1, len(question)):
            print("{}. {}".format(i, question[i]))
        answer = input("What is your answer? ")
        answers.append(answer)
    return answers

def check_answers(questions, answers):
    score = 0
    for i in range(len(questions)):
        if questions[i][int(answers[i])] == questions[i][1]:
            score += 1
    return score

# 4. Country Cities Guessing Game Python Project
import requests
import json
import random

def get_countries():
    url = "https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-capital-city.json"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def get_country(data):
    country = random.choice(data)
    return country

def get_capital(country):
    capital = country["city"]
    return capital

def get_answer(country):
    answer = input("What is the capital of {}? ".format(country))
    return answer

