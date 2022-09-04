# country - capital city guesser

import random
import json
import requests



def fetch_country_data():
    """Fetches country data from the web"""
    url = "https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-capital-city.json"
    response = requests.get(url)
    return response.json()


def get_random_country(country_data):
    """Returns a random country"""
    return random.choice(country_data)


def get_country_name(country):
    """Returns the name of a country"""
    return country["country"]

def get_country_capital(country):
    """Returns the capital of a country"""
    return country["city"]

def get_user_input(ctry_name):
    """Returns the user input"""
    return input(f"What is the capital city of {ctry_name}? ")

def is_valid_input(user_input):
    """Checks if the user input is valid"""
    if user_input == "q" or user_input == "Q":
        return True
    elif not isinstance(user_input, str):
        return True
    else:
        return False

def is_correct_answer(user_input, country):
    """Checks if the user input is correct"""
    if user_input == get_country_capital(country):
        return True
    else:
        return False

def main():
    """Main function"""
    user_points = 0
    country_data = fetch_country_data()
    while True:
        country = get_random_country(country_data)
        user_input = get_user_input(get_country_name(country))  
        if is_valid_input(user_input):
            print("Thanks for playing!, your final score is: ", user_points if user_points > 0 else 0)
            break
        elif is_correct_answer(user_input, country):
            user_points += 5
            print(f"Correct! The capital of {get_country_name(country)} is {get_country_capital(country)}")
        else:
            user_points -= 2
            print(f"Wrong! The capital of {get_country_name(country)} is {get_country_capital(country)}")

if __name__ == "__main__":
    main()