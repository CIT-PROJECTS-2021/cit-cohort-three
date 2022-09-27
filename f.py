import random
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from dateutil import parser



class CreditCard:
    def __init__(self, name):
        self.name = name
        self.card_number = self.generate_card_number()
        self.expiration_date = self.generate_expiration_date()
        self.cvv = self.generate_cvv()
        
    def generate_card_number(Self):
        return "4567" + str(random.sample(range(33, 70), 6)) + datetime.now().strftime("%Y%m%d")

    def generate_expiration_date(Self):
        return datetime.now() + relativedelta(years=5)

    def generate_cvv(Self):
        return random.sample(range(33, 70), 3)

    def __str__(self):
        return f"Name: {self.name}, Card Number: {self.card_number}, Expiration Date: {self.expiration_date}, CVV: {self.cvv}"


card = CreditCard("John Doe")
print(card)