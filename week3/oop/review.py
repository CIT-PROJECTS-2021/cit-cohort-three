from functools import reduce


age = int(input("Enter your age: "))

if age < 18:
    print("You are not old enough to vote")
else:
    print("You are old enough to vote")


for age in range(5, 100, 5):
    if age < 13:
        print("You are a child")
    elif age < 20:
        print("You are a teenager")
    elif age < 35:
        print("You are a young adult")
    elif age < 65:
        print("You are an adult")
    else:
        print("You are an elder")


shop = ["bread", "milk", "eggs", "cheese", "butter"]

half = len(shop) // 2

left = shop[:half]
right = shop[half:]


for item in left:
    print(f"Left: {item}")

for item in right:
    print(f"Right: {item}")


for i in range(len(shop)):
    print(f"Item {i}: {shop[i]}")



for item in range(10):
    print(item)
else:
    print("Loop finished")


my_tuple = (1,)
my_list = [1,2,3]
my_dict = {"a": 1, "b": 2, "c": 3}

uganda = "Uganda"
count = 0
while count < len(uganda):
    count += 1

print(f"{uganda} has {count} letters")



def add(x, y=5):
    return x + y

print(add(2, 3))


print(add(y=10, x=5))
print(add(x=7))
print(add(x=8, y=9))

# print(add(x=8, 9))
print(add(8, y=9))

def add(*args):
    print(sum(args))

add(1, 2, 3)


def add(**kwargs):
    print(sum(kwargs.values()))
    print(kwargs.get('a') - kwargs.get('b'))
    


add(a=1, b=2, c=3)


squares = lambda x: x * x

for i in range(1, 10):
    print(squares(i))


add = lambda x, y: x + y
print(add(2, 3))

mul = lambda x, y, z: x * y * z
print(mul(2, 3, 4))

add = lambda *args: sum(args)

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])