# static methods are methods that are not bound to an instance of a class


class Animal:
    def __init__(self, name):
        self.name = name

    @staticmethod          # static method decorator
    def get_animal_type(): # static method
        return "animal"

    def change_name(self, new_name):
        self.name = new_name

    @staticmethod
    def make_sound(sound):
        print(sound)


print(Animal.get_animal_type())
animal = Animal("dog")
print(animal.get_animal_type())


class Calculator:
    def addNumbers(x, y):
        return x + y


Calculator.addNumbers = staticmethod(Calculator.addNumbers)
print(Calculator.addNumbers(2, 3))


class Student:
    # attributes bound to the class
    school_name = "CIT" # class variable

    def __init__(self, name, age): # constructor
        # attributes bound to the object
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, name):  # cls is a reference to the class
        cls.school_name = name
        # Student.school_name = name


print(Student.school_name)
jesica = Student("Jesica", 20)
Student.change_school("MIT")
print(Student.school_name)
print(jesica.school_name)


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


user = User("Jesica", User.hash_password("1234"))
print(user)