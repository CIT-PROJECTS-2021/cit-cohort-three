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


ANSWER FOR OCHOLE ROGERS

# BankAccount class
class Bankaccount:
	def __init__(self):

# Function to deposite amount
def deposit(self):
		amount = float(input("Enter amount to be deposited: "))
		self.balance += amount
		print("\n Amount Deposited:", amount)
        
# Function to withdraw the amount
def withdraw(self):
		amount = float(input("Enter amount to be withdrawn: "))
		if self.balance >= amount:
			self.balance -= amount
			print("\n You Withdrew:", amount)
		else:
			print("\n Insufficient balance ")

# Function to display the amount
def display(self):
		print("\n Net Available Balance =", self.balance)

# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:
	def __init__(self):
		self.balance=0
		print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\n Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("\n You Withdrew:", amount)
		else:
			print("\n Insufficient balance ")

	def display(self):
		print("\n Net Available Balance=",self.balance)

# Driver code

# creating an object of class
s = Bank_Account()

# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()

    

    


