# count = 10

# if count > 20:
#     print("Count is greater")
# else:
#     print("Count is not greater")

# # If..elif..elif..else
is_fanta = False
is_coke = True
is_mirinda = False

if is_fanta:
    print("Buying fanta")
elif is_coke:
    print("Buying Coke")
elif is_mirinda:
    print("Buying Mirinda")
else:
    print("Buying water")

is_raining = False
is_sunny = True
voting_age = 18

age = int(input("How old are you? "))

if age >= voting_age:
    if is_raining:
        print("Please move with your umbrella and go to vote")

    elif is_sunny:
        print("Please wear light clothes and go to vote")

    else:
        print("Please wear normal clothes")
else:
    print("Sorry you are unable to go for voting!")


# Write a program that converts temperatures
# based on the choice of the user.
# The figures should be from user user input.
#  use if statement to check which conversion the user
#  wants to perform
FAHRENHEIT = 1
CELICIUS = 2
KELVIN = 3

user_choice = int(input(
    "Enter 1 for Fahrenheit to Celsius, 2 for Celsius to Fahrenheit, 3 for Kelvin to Fahrenheit: "))

if user_choice == FAHRENHEIT:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(str(fahrenheit) + " degrees in Fahrenheit is " +
          str(celsius) + " degrees in Celsius")
elif user_choice == CELICIUS:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print(str(celsius) + " degrees in Celsius is " +
          str(fahrenheit) + " degrees in Fahrenheit")
elif user_choice == KELVIN:
    kelvin = float(input("Enter temperature in Kelvin: "))
    fahrenheit = kelvin * 9/5 - 459.67
    print(str(kelvin) + " degrees in Kelvin is " +
          str(fahrenheit) + " degrees in Fahrenheit")
else:
    print("Invalid choice")
