#OOP

class Car:
    def __init__(self, model, make, color, year):
        self.model = model
        self.make = make
        self.color = color
        self.__year = year #private variable

    def move(self, speed=0):
        if speed > 0:
            print(f"Moving at {speed} mph")
        else:
            print("Not moving")

    def stop(self):
        print("Stopping")

    def set_year(self, year):
        self.__year = year

    def get_year(self):
        return self.__year


car = Car("Toyota", "Corolla", "Red", 2019)
# print(car)
print(f"Initial year: {car.get_year()}")
car.move(5)
car.stop()
car.set_year(2022)
print(f"New year: {car.get_year()}")
# print(car.__year)

#Inheritance
class AmericanCar(Car):
    def __init__(self, model, make, color, year, manufacturer):
        
        super().__init__(model, make, color, year)
        self.__year = year
        self.manufacturer = manufacturer

    def set_year(self, year):
        self.__year = year

    def get_year(self):
        return self.__year

ford = AmericanCar("Ford", "Mustang", "Red", 2019, "Ford")
ford.move(10)


class IndianCar(Car):
    def sing(self):
        print("Vande Mataram")

tata = IndianCar("Tata", "Nano", "White", 2019)
tata.sing()
tata.move(5)
print(tata.get_year())
print(tata.model)



class A:
    def __init__(self):
        print("A")

    def a(self):
        print("a")

class B:
    def __init__(self):
        print("B")

    def b(self):
        print("b")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("C")

    def c(self):
        print("c")

c = C()
c.a()
c.b()
c.c()


class Employee:
    def __init__(self, name, salary):
        self.name = name # public
        self.__salary = salary #private variable
        # self._id = 453 # protected variable

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary


emp = Employee("John", 1000)
print(emp.name)
print(emp.get_salary())
emp.set_salary(2000)
print(emp.get_salary())
# print(emp.__salary)


class Customer(Employee):
    def __init__(self, name, salary, customer_id):
        super().__init__(name, salary)
        self.customer_id = customer_id

    def get_id(self):
        return self.customer_id


cust = Customer("John", 1000, 123)
print(cust.get_salary())

# _classname__dataMember name mangling
print(emp._Employee__salary)




class Company:
    def __init__(self):
        self._employees = []

    def add_employee(self, employee):
        self._employees.append(employee)


class Google(Company):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def count_employees(self):
        return len(self._employees)


google = Google("Google")
google.add_employee("John")
google.add_employee("Jane")
print(google.count_employees())
for emp in google._employees:
    print(emp)


# Polymorphism
print("Polymorphism")
print(123)
print([1, 2, 3])
print({"a": 1, "b": 2})

len("Hello") # ---> counting characters
len([1, 2, 3]) # ---> counting elements
len({"a": 1, "b": 2}) # ---> counting keys


class Shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Square(Shape):
    def __init__(self, length):
        super().__init__(length, length)

    def area(self):
        return self.length * self.length


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)

    def area(self):
        return 0.5 * self.length * self.breadth

square = Square(5)
print(f"Square area: {square.area()}")
rectangle = Rectangle(5, 10)
print(f"Rectangle area: {rectangle.area()}")
triangle = Triangle(5, 10)
print(f"Triangle area: {triangle.area()}")