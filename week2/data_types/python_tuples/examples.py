# Programs to help you understand tuples

# 1. A program to create a tuple with different data types
from typing import Any


def create_tuple():
    tup = (1, 2.0, "3", True)
    print(tup)
    return tup

# 2. A program to create a tuple from a list
def create_tuple_from_list(lst: list) -> tuple:
    if not isinstance(lst, list):
        raise ValueError(f"{lst} is not a list")

    return tuple(lst)

# 3. A program to print nested tuple
def print_nested_tuple(tup: tuple):
    for item in tup:
        if isinstance(item, tuple) or isinstance(item, list):
            print_nested_tuple(item)
        else:
            print(item)


nested_tuple = (1, 2, (3, 4, (5, 6, 7), "Hello"), "World")
print_nested_tuple(nested_tuple)


# 4. A program to print the length of a tuple
def print_tuple_length(tup: tuple) -> int:
    return len(tup)


# 5. A program to print the maximum and minimum elements of a tuple
def print_max_min_tuple(tup: tuple) -> Any:
    return max(tup), min(tup)


# 6. A program to print the elements of a tuple in reverse order
def print_tuple_in_reverse(tup: tuple) -> None:
    for item in reversed(tup):
        print(item)


# 7. A program to print the first and last elements of a tuple
def print_first_last_tuple(tup: tuple) -> None:
    print(f"first item: {tup[0]}")
    print(f"last item: {tup[-1]}")


# 8. Convert characters in a tuple into a string. eg: ('a', 'b', 'c') -> 'abc'
def convert_tuple_to_string(tup: tuple) -> str:
    return "".join(tup)


# 9. A program to print the middle element of a tuple
def print_middle_tuple(tup: tuple) -> None:
    print(tup[len(tup) // 2])


# 10. A program to print the middle element of a tuple if the tuple is even length
def print_middle_tuple_if_even(tup: tuple) -> None:
    if len(tup) % 2 == 0:
        print(tup[len(tup) // 2])


# 11. A program to print the middle element of a tuple if the tuple is odd length
def print_middle_tuple_if_odd(tup: tuple) -> None:
    if len(tup) % 2 == 1:
        print(tup[len(tup) // 2])



# 12. A program to print the middle element of a tuple if the tuple is odd length
def print_middle_tuple_if_odd_even(tup: tuple) -> None:
    if len(tup) % 2 == 0:
        print(tup[len(tup) // 2])
    else:
        print(tup[len(tup) // 2 - 1])



        