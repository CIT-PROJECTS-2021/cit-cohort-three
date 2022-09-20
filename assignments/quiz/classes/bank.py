# Bank class
# user can create account, deposit, withdraw, transfer, 
# check balance, check history, and exit
# user can only withdraw if they have enough money in their account
# user can only transfer if they have enough money in their account
# user has name, phone number, pin
# account number is generated automatically
# user details and transaction history are stored in mysql database
# user can only access their own account
# user can only access their own transaction history
# user can only access their own account number
# user details are entered by user

import sys
import os
import secrets
import hashlib
import mysql.connector
import re
from time import sleep
from datetime import datetime


class Bank:
    def __init__(self, name, phone, pin):
        self.name = name
        self.phone = phone
        self.pin = hashlib.sha256(pin.encode()).hexdigest()
        self.account_number = self.create_account_number()
        self.balance = 0
        self.account_number_login = ''
        self.create_database()


    def connect_db(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='cit_bank'
            )
        except:
            raise mysql.connector.Error("Could not connect to database")

        c = conn.cursor()
        return conn, c


    def create_database(self):
        conn, c = self.connect_db()
        c.execute('''CREATE TABLE IF NOT EXISTS bank(id INT PRIMARY KEY AUTO_INCREMENT, 
        name VARCHAR(255), phone VARCHAR(10), pin VARCHAR(255),
        account_number VARCHAR(255) NOT NULL UNIQUE, balance INT) ''')
        c.execute('''CREATE TABLE IF NOT EXISTS transactions(
            id INT PRIMARY KEY AUTO_INCREMENT,
            account_number VARCHAR(255) NOT NULL,
            transaction_type VARCHAR(255) NOT NULL,
            amount INT NOT NULL,
            date DATETIME default CURRENT_TIMESTAMP
        )''')

        conn.commit()
        conn.close()
        print("Database created!")


    def create_account_number(self):
        # account number format: 
        # AC+last 4 digits of phone number+current date+random number 
        # and account number max length 15
        # AC13592022091972346589137
        account_number = 'AC' + \
            self.phone[-4:] + datetime.now().strftime('%Y%m%d') + \
            str(secrets.randbits(15))
        return account_number


    def create_account(self):
        conn, c = self.connect_db()
        sql = ('''
        INSERT INTO bank(name, phone, pin, account_number, balance)
        VALUES(%s, %s, %s, %s, %s)
        ''')
        data = (self.name, self.phone, self.pin, self.account_number, self.balance)

        try:
            c.execute(sql, data)
            conn.commit()
            print('Account created \n Your account number is {}'.format(self.account_number))
        except mysql.connector.Error as err:
            print('Error: {}'.format(str(err)))
            conn.rollback()
        finally:
            c.close()
            conn.close()


    def get_balance(self):
        conn, c = self.connect_db()
        c.execute('''
        SELECT balance FROM bank WHERE account_number = %s
        ''', (self.account_number_login,))

        data = c.fetchone()
        conn.close()
        return data[0]


    def check_balance(self):
        print("Your current balance is: {}".format(str(self.get_balance())))


    def update_database(self, t_type, amount):
        conn, c = self.connect_db()
        c.execute('''
        UPDATE bank SET balance = %s WHERE account_number = %s
        ''', (self.balance, self.account_number_login))
        c.execute('''
        INSERT INTO transactions(account_number, transaction_type, amount)
        VALUES(%s, %s, %s)
        ''', (self.account_number_login, t_type, amount))

        conn.commit()
        conn.close()
        print('Database updated!')


    def deposit(self, amount):
        self.balance = self.get_balance() + amount
        self.update_database("deposit", amount)
        print('Deposit successful')
        self.check_balance()


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.get_balance() - amount
            self.update_database("withdraw", amount)
            print("You have withdrawn UGX {}".format(str(amount)))
            self.check_balance()
        else:
            print("Insufficient balance")

    
    def transfer(self, amount, account_number):
        if amount <= self.get_balance():
            if self.transfer_to_account(account_number, amount):
                self.balance = self.get_balance() - amount
                self.update_database("transfer", amount)
                print("Transfer successful \n You transferred {} to {}".format(str(amount), account_number))
                self.check_balance()
        else:
            print("Insufficient balance")


    def transfer_to_account(self, account_number, amount):
        conn, c = self.connect_db()
        c.execute('''
        SELECT account_number, balance FROM bank WHERE account_number = %s
        ''', (account_number,))
        data = c.fetchone()
        if data is None:
            print('Account number does not exist')
            return False
        else:
            if data[0] == self.account_number_login:
                print('You cannot transfer to your own account')
                return False
            else:
                c.execute('''
                UPDATE bank SET balance = %s WHERE account_number = %s
                ''', (data[1]+amount, account_number))
                conn.commit()
                conn.close()
                return True

    
    def login(self, account_number, pin):
        conn, c = self.connect_db()
        c.execute('''SELECT * FROM bank WHERE account_number = %s''', (account_number,))
        data = c.fetchone()
        conn.close()

        if data is None:
            print('Account Number does not exist')
        
        else:
            hashed_pin = hashlib.sha256(pin.encode()).hexdigest()
            if hashed_pin == data[3]:
                self.account_number_login = data[4]
                self.balance = data[5]
                print('Login successful')
                return True
            else:
                print("Incorrect PIN")
                return False

    def check_history(self):
        conn, c = self.connect_db()
        c.execute('''
        SELECT  * FROM transactions WHERE account_number = %s
        ''', (self.account_number_login,))
        data = c.fetchall()
        c.close()
        conn.close()
        print('Your transaction history: ')
        for row in data:
            # Transfer of UGX: 5000 on Jan 19
            print(row[2] + ' of UGX: ' + str(row[3]) + ' on ' + str(row[4]))


    def exit(self):
        print('Thank you for using CIT Bank')
        sys.exit()


# clear screen function
def clear_screen():
    sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
        

def check_phone(phone_number):
    return re.match(r'^(077|078|076|070|075)\d{7}$', phone_number)


def main(Bank):
    print('Welcome to CIT Bank')
    print('1. create account \n 2. Login \n 3. Exit')
    user_input = input("Enter your choice: ")

    if user_input == '1':
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")

        while not check_phone(phone):
            print("Invalid phone number")
            phone = input("Enter your phone number: ")

        pin = input("Enter your pin: ")

        if not name or not phone or not pin:
            print('cannot create account, All fields are required')
            clear_screen()
            sys.exit(-1)
        else:
            bank = Bank(name, phone, pin)
            bank.create_account()
    elif user_input == "2":
        account_number = input('Enter your account number: ')
        pin = input('Enter your PIN: ')
        bank = Bank('', '', '')
        if bank.login(account_number, pin):
            while True:
                print('Welcome Back')
                print('1. Deposit\n2. Withdraw\n3. Transfer\n4. Check Balance\n5.Check History\n6. Exit')
                user_input = input('Enter your choice: ')
                
                if user_input == '1':
                    amount = int(input('Enter the amount you want to deposit: '))
                    bank.deposit(amount)
                    clear_screen()
                elif user_input == '2':
                    amount = int(input('Enter the amount you want to withdraw: '))
                    bank.withdraw(amount)
                    clear_screen()
                elif user_input == '3':
                    amount = int(input('Enter the amount you want to transfer: '))
                    account_number = input('Enter the account number you want to transfer to: ')
                    bank.transfer(amount, account_number)
                    clear_screen()
                elif user_input == '4':
                    bank.check_balance()
                    clear_screen()
                elif user_input == '5':
                    bank.check_history()
                    clear_screen()
                elif user_input == '6':
                    bank.exit()
                else:
                    print('Invalid option!')
        else:
            print('Login failed :(')
            clear_screen()

    elif user_input == '3':
        sys.exit()
    else:
        print("Invalid input")
        sys.exit(-1)


if __name__ == '__main__':
    main(Bank)
