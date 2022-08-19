# +, -, *, /, //, %, **, <, >, <=, >=, ==, !=, <>

x = 6
y = 3

print(f"x + y = {x+y}")

print(f"x - y = {x - y}")

print(f"x * y = {x * y}")

print(f"x / y = {x / y}")

print(f"x // y = {x // y}")

print(f"x ** y = {x ** y}")

print(f"x % y = {x % y}")

# f string

# formating string
print("x / y = {}".format(x /y))


a = 5

a += 5  # a = a + 5

print(a)

b = 9

b -= 4  # b = b - 4

print(b)

c = 8

c &= 3  # c = c & 3 -> 8
# c = c & 3 -> 0 | False
# 1000  11
# The & operator is used to perform a BITWISE AND operation on two nubers


print(c)

d = 7

d |= 5

print(d)


voting_age = 18

my_age = int(input("Enter your age: "))
is_reg = int(input("Enter 1 if registred or 0 if not: "))

if my_age >= voting_age & is_reg == 1:

    print("You are allowed to vote")
else:
    print("You are not allowed to vote")

