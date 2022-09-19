# 1. Using classes, Create a basic banking application with the following features:

#     1. Create a class called `BankAccount` with the following attributes:

#         1. `account_number` - a string
#         2. `balance` - a float
#         3. `owner` - a string
#         4. `type` - a string

class BankAccount:
    def __init__(self, account_number, balance, owner, type ):
        self.account_number=account_number
        self.balance=balance
        self.owner=owner
        self.type=type

    def __str__(self):
        return f"Account Number: {self.account_number} \nBalance: {self.balance} \nOwner: {self.owner} \nType: {self.type} "

    

#     2. Create a class called `Bank` with the following attributes:

#         1. `name` - a string
#         2. `accounts` - a list of `BankAccount` objects
class Bank:
    def __init__(self, name, accounts):
        self.name=name
        self.accounts=accounts

    def __str__(self):
        return f"Bank Name: {self.name}"

    def add_account(self, account):
        self.accounts.append(account)

#     3. Create a class called `Customer` with the following attributes:

#         1. `name` - a string
#         2. `accounts` - a list of `BankAccount` objects
class Customer:
    def __init__(self, name, accounts):
        self.name=name
        self.accounts=accounts 
    
    def __str__(self):
        return f"Customer Name: {self.name}"

    def add_account(self, account):
        self.accounts.append(account)

#     4. Create a class called `Transactions` with the following attributes:
    
#             1. `account` - a `BankAccount` object
#             2. `amount` - a float
#             3. `type` - a string
class Transactions:
    def __init__(self, account, amount, type):
        self.account=account
        self.amount=amount
        self.type=type

    def post_transaction(self):
        if self.type == "Deposit":
            self.account.balance = self.account.balance + self.amount
        elif self.type == "Withdraw" and self.account.balance >= self.amount:
            self.account.balance = self.account.balance - self.amount
        else:
            return "insufficient balance"




#     The application should have the following functionality:

#     1. Create a new `Bank` object
My_bank = Bank("DTB", [])

#     2. Create a new `Customer` object
bank_customer = Customer("Tonny Kakooza", [])

#     3. Create a new `BankAccount` object
bank_account = BankAccount("7112991001", 5000, "Tonny Kakooza", "Digital savings")

#     4. Add the `BankAccount` object to the `Bank` object
My_bank.add_account(bank_account)

#     5. Add the `BankAccount` object to the `Customer` object
bank_customer.add_account(bank_account)

#     6. Print the `Bank` object
print(My_bank)

#     7. Print the `Customer` object
print(bank_customer)

#     8. Print the `BankAccount` object
print(bank_account)

#     9. Create a new `Transaction` object
my_transaction = Transactions(bank_account, 10000, "Deposit")
#     10. Add the `Transaction` object to the `BankAccount` object
my_transaction.post_transaction()
    

    

