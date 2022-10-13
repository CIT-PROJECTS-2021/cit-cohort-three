import random


class BankAccount:

    @staticmethod
    def generate_account_number():
        return random.randint(100000000, 999999999)


# This is a change

class Customer:

    def __init__(self, name, address, account):
        self.name = name
        self.address = address
        self.account = account
        self.account_number = BankAccount.generate_account_number()

    def __str__(self):
        return f"Customer: {self.name} \t Account Number: {self.account_number}"


    def change_password(self, old_password, new_password):
        if old_password == self.password:
            self.password = new_password
            return True
        else:
            return False

class BankUser(Customer):
    def __init__(self, name, address, account, password):
        super().__init__(name, address, account)
        self.password = password

    def __str__(self):
        return f"Customer: {self.name} \t Account Number: {self.account_number} \t Password: {self.password}"


def main():
    customer = Customer("John Doe", "123 Main St", "Checking")
    print(customer)
    user = BankUser("Jane Doe", "123 Main St", "Checking", "password")
    print(user)
    user.change_password("password", "new_password")
    print(user)

main()
