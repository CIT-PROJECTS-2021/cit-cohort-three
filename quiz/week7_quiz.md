# END OF WEEK 7 QUIZ

1. Your task is to create slightly different animals, which should have the same properties and methods, but should implement the talk() method in different ways. For example. should a cat (when talking) say "Moew", a dog "Woff", a fish "Blub" and a Cow "Muuu". They should all share the following (private) properties: name (string), age (number), food (list of strings), and have the functions get_name, set_name, get_age, set_age, get_food, add_food, remove_food. Finally, all the animals must have the talk function, but that function must, as I said, be implemented in each animal, as the animals have different sounds.

When you have made the classes, create instances of the classes and put in a list - loop through the list - and let all the animals talk! :)

2. The snail climbs up 7 feet each day and slips back 2 feet each night. 
How many days will it take the snail to get out of a well with the given depth?. Using python, write a function to solve this problem.
Sample Input: 31
Sample Output: 6

function main() {
    var depth = parseInt(readLine(), 10);
    //your code goes here
    var day = 0;
    var total = 0;
    while(total<depth){
        day = day + 1;
        total = total + 7;
        if(total >= depth){
            console.log(day);
            break;
        }
        total = total - 2;
    }
}


3. Write a function that takes a list of numbers and returns the largest number in the list.

# Python program to find largest
# number in a list
 
# list of numbers
list1 = [10, 20, 4, 45, 99]
 
# sorting the list
list1.sort()
 
# printing the last element
print("Largest element is:", list1[-1])

4. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
`Hello world!`
Then, the output should be:
`UPPER CASE 1`
`LOWER CASE 9`

def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')


5. Using Object Oriented Programming, write a program that implements
a dice game. The game should have two players, and each player
should have a name and a score. The game should have a method
called `play` that takes two players as arguments and simulates
the game. The game should be played as follows:
    - Each player rolls a die.
    - The player with the highest roll wins the round.
    - The winner gets one point added to their score.
    - The game ends when one player has 5 points.
    - The player with the most points at the end of the game wins.
    - The program should print out the winner's name and score.
    - If a player rolls a 6, they get an extra roll. If they roll a 6 again, they get another extra roll. If they roll a 6 a third time, they get an extra roll, but their turn ends.

# dice.py

# ~~~ App's main code block ~~~
# 1. Get and validate user's input
num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = parse_input(num_dice_input)
# dice.py

def parse_input(input_string):
    """Return `input_string` as an integer between 1 and 6.

    Check if `input_string` is an integer number between 1 and 6.
    If so, return an integer with the same value. Otherwise, tell
    the user to enter a valid number and quit the program.
    """
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)

# ~~~ App's main code block ~~~
# dice.py
import random

# ...

def roll_dice(num_dice):
    """Return a list of integers with length `num_dice`.

    Each integer in the returned list is a random number between
    1 and 6, inclusive.
    """
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results
# 1. Get and validate user's input
num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = parse_input(num_dice_input)
# 2. Roll the dice
roll_results = roll_dice(num_dice)

print(roll_results)  # Remove this line after testing the app

6. Write a Python program that lists out all the default as well as custom properties of the class.

class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age

teacher = Teacher("Lokesh", 36)
print("Teacher class's object  all properties")

print(dir(teacher))

7. Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal methods.

# Python program to
# demonstrate stack implementation
# using list
 
stack = []
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)
 
# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty

8. Using list comprehension, write a program that takes a list of numbers and returns a list of the squares of the numbers.

# create a list with 7 integer elements
data=[1,2,3,4,5,6,7]
 
# use list comprehension to get square
# of odd numbers
result = [i*i for i in data if i%2!=0]
 
# display the result
print(result)

9. Using only functions and lists, Implement a queue data structure. The queue should have the following methods: enqueue, dequeue, and size. The queue should be "first-in-first-out" (FIFO).

# Python3 program for array implementation of queue
 
# Class Queue to represent a queue
class Queue:
 
    # __init__ function
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity -1
        self.Q = [None]*capacity
        self.capacity = capacity
     
    # Queue is full when size becomes
    # equal to the capacity
    def isFull(self):
        return self.size == self.capacity
     
    # Queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0
 
    # Function to add an item to the queue.
    # It changes rear and size
    def EnQueue(self, item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("% s enqueued to queue"  % str(item))
 
    # Function to remove an item from queue.
    # It changes front and size
    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return
         
        print("% s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size -1
         
    # Function to get front of queue
    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")
 
        print("Front item is", self.Q[self.front])
         
    # Function to get rear of queue
    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is",  self.Q[self.rear])
 
 
# Driver Code
if __name__ == '__main__':
 
    queue = Queue(30)
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.DeQueue()
    queue.que_front()
    queue.que_rear()

10. Using a while loop, implement merge sort algorithm.

# Recursive Python Program for merge sort
  
def merge(left, right):
    if not len(left) or not len(right):
        return left or right
  
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break 
  
    return result
  
def mergesort(list):
    if len(list) < 2:
        return list
  
    middle = int(len(list)/2)
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
  
    return merge(left, right)
      
seq = [12, 11, 13, 5, 6, 7]
print("Given array is")
print(seq); 
print("\n")
print("Sorted array is")
print(mergesort(seq))
