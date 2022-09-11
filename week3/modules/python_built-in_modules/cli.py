# A command line application that consumes https://api-v3.safe-courier.ml api

import argparse
import sys
import requests
import json
import pickle
import os
from tabulate import tabulate
from colorama import init, Fore, Back, Style

# Initialize colorama
init()

# The base url for the api
base_url = "https://api-v3.safe-courier.ml/api/v1"

# The headers for the api
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# The api endpoints
endpoints = {
    "login": "/auth/login",
    "register": "/auth/register",
    "users": "/users",
    "parcels": "/parcels",
}


def make_request(url, method, data=None, headers=None):
    """Make a request to the api"""
    if method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "POST":
        response = requests.post(url, headers=headers, data=data)
    elif method == "PUT":
        response = requests.put(url, headers=headers, data=data)
    elif method == "DELETE":
        response = requests.delete(url, headers=headers)
    else:
        raise Exception("Invalid method")
    return response


def check_auth():
    # check if .safe_courier file exists in home directory and has token inside
    if os.path.isfile(os.path.expanduser("~/.safe_courier")):
        with open(os.path.expanduser("~/.safe_courier"), "rb") as f:
            token = pickle.load(f)
            headers["Authorization"] = f"Bearer {token}"
            return True
    else:
        return False


def login():
    # check if user is already logged in
    if check_auth():
        print("You are already logged in, would you like to re-login? (y/n): ")
        choice = input()
        if choice.lower() == "n":
            return
    # Login to the api
    email = input("Email: ")
    password = input("Password: ")

    if not email or not password:
        print(Fore.RED + "Email and password are required" + Style.RESET_ALL)
        return

    data = {
        "email": email,
        "password": password
    }
    response = make_request(
        base_url + endpoints["login"], "POST", json.dumps(data), headers)
    if response.status_code == 200:
        data = response.json()
        with open(os.path.expanduser("~/.safe_courier"), "wb") as f:
            pickle.dump(data["access_token"], f)
        headers["Authorization"] = f"Bearer {data['access_token']}"
        # use colorama to print in green
        print(Fore.GREEN + "Login successful, logged in as {}".format(data["user"]["email"]) + Style.RESET_ALL)
    else:
        print(Fore.RED + "Login failed, {}".format(response.json()["message"]) + Style.RESET_ALL)
    return

def logout():
    # Logout from the api
    if check_auth():
        os.remove(os.path.expanduser("~/.safe_courier"))
        print(Fore.GREEN + "Logout successful" + Style.RESET_ALL)
    else:
        print(Fore.RED + "You are not logged in" + Style.RESET_ALL)
    return


def check_email(email):
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def register():
    # Register to the api 
    email = input("Email: ")
    password = input("Password: ")
    username = input("Username: ")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    address = input("Address: ")
    phone = input("Phone number: ")

    if not email or not password or not username or not first_name or not last_name or not address or not phone:
        print(Fore.RED + "All fields are required" + Style.RESET_ALL)
        return

    if not check_email(email):
        print(Fore.RED + "Invalid email" + Style.RESET_ALL)
        return

    data = {
        "email": email,
        "password": password,
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "address": address,
        "phone": phone
    }

    response = make_request(
        base_url + endpoints["register"], "POST", json.dumps(data), headers)
    if response.status_code == 201:
        print(Fore.GREEN + "Registration successful" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Registration failed, {}".format(response.json()["message"]) + Style.RESET_ALL)
    return

def get_users():
    # Get all users
    response = make_request(
        base_url + endpoints["users"], "GET", headers=headers)
    if response.status_code == 200:
        data = response.json()
        # tabulate_output(data)
        print(json.dumps(data, indent=4))
    else:
        print("Failed to get users, {}".format(response.json()["message"]))
    return


def get_parcels():
    # Get all parcels
    response = make_request(
        base_url + endpoints["parcels"], "GET", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))
    else:
        print("Failed to get parcels, {}".format(response.json()["message"]))
    return


def create_parcel():
    # Create a parcel
    name = input("Name: ")
    weight = input("Weight: ")
    price = input("Price: ")
    data = {
        "name": name,
        "weight": weight,
        "price": price
    }
    response = make_request(
        base_url + endpoints["parcels"], "POST", json.dumps(data), headers)
    if response.status_code == 201:
        print("Parcel created successfully")
    else:
        print("Failed to create parcel, {}".format(response.json()["message"]))
    return

def tabulate_output(data):
    # print data as a table in the console.
    # use dictionary keys as table headers
    # use dictionary values as table rows
    print(tabulate(data, headers="keys"))



def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--login", help="Login to the api", action="store_true")
    parser.add_argument("-r", "--register",
                        help="Register to the api", action="store_true")
    parser.add_argument(
        "-u", "--users", help="Get all users", action="store_true")
    parser.add_argument("-p", "--parcels",
                        help="Get all parcels", action="store_true")
    parser.add_argument(
        "-c", "--create", help="Create a parcel", action="store_true")

    parser.add_argument("-lg", "--logout", help="Logout from the API", action="store_true")

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    if args.login:
        login()
    elif args.register:
        register()
    elif args.users or args.create or args.parcels or args.logout:
        # Check if user is logged in
        if check_auth():
            if args.users:
                get_users()
            elif args.parcels:
                get_parcels()
            elif args.create:
                create_parcel()
            elif args.logout:
                logout()
            else:
                parser.print_usage()
        else:
            print("You need to be authenticated to perform that action")
            sys.exit()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()