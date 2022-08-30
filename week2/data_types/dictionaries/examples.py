# Programs to help you understand dictionaries

# 1. a program to create a dictionary with different data types
from typing import Any


def create_dictionary():
    dic = {"key1": 1, "key2": 2.0, "key3": "3", "key4": True}
    print(dic)
    return dic

# 2. a program to create a dictionary from a list
def create_dictionary_from_list(lst: list) -> dict:
    if not isinstance(lst, list):
        raise ValueError(f"{lst} is not a list")

    return dict(lst)

# 3. a program to print nested dictionary
def print_nested_dictionary(dic: dict):
    for key, value in dic.items():
        if isinstance(value, dict) or isinstance(value, list):
            print_nested_dictionary(value)
        else:
            print(f"{key}: {value}")


nested_dictionary = {"key1": 1, "key2": 2, "key3": {"key4": 4, "key5": 5, "key6": {"key7": 7, "key8": 8}}}
print_nested_dictionary(nested_dictionary)

#. A simple user system using dictionaries, lists and tuples
def create_user_system():
    users = {}
    while True:
        print("1. Create user")
        print("2. Delete user")
        print("3. Print users")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            users[username] = password
        elif choice == "2":
            username = input("Enter username: ")
            if username in users:
                del users[username]
            else:
                print("User not found")
        elif choice == "3":
            for username, password in users.items():
                print(f"Username: {username}, Password: {password}")
        elif choice == "4":
            break
        else:
            print("Invalid choice")


create_user_system()


# 4. create a dictionary with keys and values using comprehension
def create_dictionary_with_comprehension():
    return {x: x**2 for x in range(10)}


# 5. create a program that searches a dictionary for a key and returns the value
def search_dictionary(dic: dict, key: Any) -> Any:
    if not isinstance(dic, dict):
        raise ValueError(f"{dic} is not a dictionary")

    if key in dic:
        return dic[key]
    else:
        return "Key not found"


# 6. A program that shuffles a dictionary
def shuffle_dictionary(dic: dict) -> dict:
    if not isinstance(dic, dict):
        raise ValueError(f"{dic} is not a dictionary")

    import random
    keys = list(dic.keys())
    values = list(dic.values())
    shuffled_keys = random.sample(keys, len(keys))
    shuffled_values = random.sample(values, len(values))
    return dict(zip(shuffled_keys, shuffled_values))


print(shuffle_dictionary({"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5})) 


# An ecommerce program using dictionaries
def ecommerce_program():
    products = {"1": {"name": "laptop", "price": 100}, "2": {"name": "mobile", "price": 200}}
    while True:
        print("1. Add product")
        print("2. Delete product")
        print("3. Print products")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            product_id = input("Enter product id: ")
            product_name = input("Enter product name: ")
            product_price = input("Enter product price: ")
            products[product_id] = {"name": product_name, "price": product_price}
        elif choice == "2":
            product_id = input("Enter product id: ")
            if product_id in products:
                del products[product_id]
            else:
                print("Product not found")
        elif choice == "3":
            for product_id, product_details in products.items():
                print(f"Product id: {product_id}, Product name: {product_details['name']}, Product price: {product_details['price']}")
        elif choice == "4":
            break
        else:
            print("Invalid choice")



        