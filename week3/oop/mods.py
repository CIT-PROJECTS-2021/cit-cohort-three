import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


    def __repr__(self):
        return f"User('{self.username}', '{self.password}')"

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
 
    @staticmethod
    def verify_password(password, hashed_password):
        return User.hash_password(password) == hashed_password