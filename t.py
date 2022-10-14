class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.name} is {self.color}"

    def move(self):
        print(f"{self.name} is moving at 100km/h")


class Car:
    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model

    def __str__(self):
        return f"{self.name} is {self.color} and it is a {self.model}"

    def move(self):
        print(f"{self.name} is moving")



class HomeCar(Vehicle, Car):
    def __init__(self, name, color, model, year):
        super().__init__(name, color)
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.name} is {self.color} and it is a {self.model} and it was made in {self.year}"


    def move(self):
        return super().move()


car = HomeCar("Toyota", "Red", "Camry", 2010)
print(car)
car.move()