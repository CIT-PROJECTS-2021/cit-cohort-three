# The following programs are examples of lambda functions.

# Example 1 (Normal function)
def add(x, y):
    return x + y

print(add(2, 3))

# Example 2 (Lambda function)
add = lambda x, y: x + y
print(add(2, 3))

# Example 3 (Lambda function)
powers = lambda x: x ** 2
print(powers(2))

# Example 4 (Lambda function)
multiples_of_number_until_range_exhausted = lambda x, y: [x * i for i in range(1, y + 1)]
print(multiples_of_number_until_range_exhausted(2, 5))

# Example 5 (Lambda function)
lambda_with_dictionary = lambda x: {i: i ** 2 for i in x}

print(lambda_with_dictionary([1, 2, 3, 4, 5]))

print_dictionary_values = lambda x: [i for i in x.values()]

print(print_dictionary_values(lambda_with_dictionary([1, 2, 3, 4, 5])))