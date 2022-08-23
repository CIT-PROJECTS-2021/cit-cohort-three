# Loops Assignment

# 1. Print First 10 natural numbers using while loop.
# 2. Calculate the sum of all numbers from 1 to a given number.
# 3. Write a program to print multiplication table of a given number. eg if number is 2, then output should be 2, 4, 6, 8 ...
# 4. Write a program to display only those numbers from a list that satisfy the following conditions
#   - The number must be divisible by five
#   - If the number is greater than 150, then skip it and move to the next number
#   - If the number is greater than 500, then stop the loop
# given `numbers = [12, 75, 150, 180, 145, 525, 50]`
# 5. Write a program to count the total number of digits in a number using a while loop. given number `4673453`
# 6. Display numbers from -10 to -1 using while loop

# 1. Print First 10 natural numbers using while loop.
i = 1
while i <= 10:
    print(i)
    i += 1

# 2. Calculate the sum of all numbers from 1 to a given number.
n = int(input("Enter a number: "))
sum = 0
counter = 1

while counter <= n:
    sum += counter
    counter += 1

print(sum)

print("\n")

# 3. Write a program to print multiplication table of a given number. eg if number is 2, then output should be 2, 4, 6, 8 ...
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

print("\n")

# 4. Write a program to display only those numbers from a list that satisfy the following conditions
#   - The number must be divisible by five
#   - If the number is greater than 150, then skip it and move to the next number
#   - If the number is greater than 500, then stop the loop
# given `numbers = [12, 75, 150, 180, 145, 525, 50]`
numbers = [12, 75, 150, 180, 145, 525, 50]

for n in numbers:
    if n % 5 == 0:
        if n > 150:
            continue
        if n > 500:
            break
        print(n)

# Explanation:
# First we iterate through the list and check if the number is divisible by 5.
# If it is divisible by 5, then we check if the number is greater than 150.
# If it is greater than 150, then we skip it and move to the next number.
# If it is greater than 500, then we break the loop.
# If it is not divisible by 5, then we print the number.



print("\n")

# 5. Write a program to count the total number of digits in a number using a while loop. given number `4673453`
num = 4673453
# convert number to string
num = str(num)

print(len(num))

# solution 2
num2 = 4673453
count = 0

while num2 != 0:
    # floor division
    # to reduce the last digit from number
    num2 = num2 // 10
    count = count + 1

# Explanation:
# First, we divide the number by 10 and store the result in num2.
# Then, we check if num2 is equal to 0. If it is, then we have reached the last digit.
# If it is not, then we continue dividing num2 by 10 and increment the count.
# This process is repeated until num2 is equal to 0.

# visualization
# First Iteration
# num2 = 4673453 // 10 = 467345, count = 1
# Second Iteration
# num2 = 467345 // 10 = 46734, count = 2
# Third Iteration
# num2 = 46734 // 10 = 4673, count = 3
# Fourth Iteration
# num2 = 4673 // 10 = 467, count = 4
# Fifth Iteration
# num2 = 467 // 10 = 46, count = 5
# Sixth Iteration
# num2 = 46 // 10 = 4, count = 6
# Seventh Iteration
# num2 = 4 // 10 = 0, count = 7
# Eighth Iteration
# The loop is terminated because num2 is equal to 0.

print(f"The number of digits is {count}")

print("\n")

# 6. Display numbers from -10 to -1 using while loop
i = -10
while i <= -1:
    print(i)
    i += 1

print("\n")


