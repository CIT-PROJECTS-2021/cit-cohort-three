"""
1. Using classes, Create a basic banking application with the following features:

    1. Create a class called `BankAccount` with the following attributes:

        1. `account_number` - a string
        2. `balance` - a float
        3. `owner` - a string
        4. `type` - a string

    2. Create a class called `Bank` with the following attributes:

        1. `name` - a string
        2. `accounts` - a list of `BankAccount` objects

    3. Create a class called `Customer` with the following attributes:

        1. `name` - a string
        2. `accounts` - a list of `BankAccount` objects

    4. Create a class called `Transactions` with the following attributes:
    
            1. `account` - a `BankAccount` object
            2. `amount` - a float
            3. `type` - a string


    The application should have the following functionality:

    1. Create a new `Bank` object
    2. Create a new `Customer` object
    3. Create a new `BankAccount` object
    4. Add the `BankAccount` object to the `Bank` object
    5. Add the `BankAccount` object to the `Customer` object
    6. Print the `Bank` object
    7. Print the `Customer` object
    8. Print the `BankAccount` object
    9. Create a new `Transaction` object
    10. Add the `Transaction` object to the `BankAccount` object
    
"""

import datetime
import random
import string


class BankAccount:
    def __init__(self, account_number, balance, owner, type):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.type = type

    def __str__(self):
        return f"Account Number: {self.account_number}\nBalance: {self.balance}\nOwner: {self.owner}\nType: {self.type}"

    def __repr__(self):
        return f"Account Number: {self.account_number}\nBalance: {self.balance}\nOwner: {self.owner}\nType: {self.type}"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount



class Bank:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts

    def __str__(self):
        return f"Name: {self.name}\nAccounts: {self.accounts}"

    def __repr__(self):
        return f"Name: {self.name}\nAccounts: {self.accounts}"

    def add_account(self, account):
        self.accounts.append(account)

class Customer:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts

    def __str__(self):
        return f"Name: {self.name}\nAccounts: {self.accounts}"

    def __repr__(self):
        return f"Name: {self.name}\nAccounts: {self.accounts}"

    def add_account(self, account):
        self.accounts.append(account)

class Transactions:
    def __init__(self, account, amount, type):
        self.account = account
        self.amount = amount
        self.type = type
        self.transactions = []

    def __str__(self):
        return f"Account: {self.account}\nAmount: {self.amount}\nType: {self.type}"

    def __repr__(self):
        return f"Account: {self.account}\nAmount: {self.amount}\nType: {self.type}"

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions

def main():
    # Create a new Bank object
    bank = Bank("Bank of America", [])

    # Create a new Customer object
    customer = Customer("John Doe", [])

    # Create a new BankAccount object
    account = BankAccount("123456789", 1000, "John Doe", "Checking")

    # Add the BankAccount object to the Bank object
    bank.add_account(account)

    # Add the BankAccount object to the Customer object
    customer.add_account(account)

    # Print the Bank object
    print(bank)

    # Print the Customer object
    print(customer)

    # Print the BankAccount object
    print(account)

    # Create a new Transaction object
    transaction = Transactions(account, 100, "Deposit")


    # Add the Transaction object to the BankAccount object
    account.deposit(100)

    transaction.add_transaction(transaction)
    # Print the BankAccount object
    print(account)

if __name__ == "__main__":
    main()

