# Stack Data Structure
In this lecture, you will learn about the stack data structure and its implementation in Python

A stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element inserted inside the stack is removed first.

You can think of the stack data structure as the pile of plates on top of another.

![stack](https://cdn.programiz.com/sites/tutorial2program/files/stack-of-plates_0.png)

Here, you can:

- Put a new plate on top
- Remove the top plate
- Look at the top plate

And, if you want the plate at the bottom, you must first remove all the plates on top. This is exactly how the stack data structure works.

### LIFO Principle of Stack
In programming terms, putting an item on top of the stack is called push and removing an item is called pop.

![stack](https://cdn.programiz.com/sites/tutorial2program/files/stack.png)

In the above image, although item 3 was kept last, it was removed first. This is exactly how the **LIFO (Last In First Out)** Principle works.

We can implement a stack in any programming language like C, C++, Java, Python or C#, but the specification is pretty much the same.

### Basic Operations of Stack
There are some basic operations that allow us to perform different actions on a stack.

- **Push:** Add an element to the top of a stack
- **Pop:** Remove an element from the top of a stack
- **IsEmpty:** Check if the stack is empty
- **IsFull:** Check if the stack is full
- **Peek:** Get the value of the top element without removing it

### Working of Stack Data Structure
The operations work as follows:

1. A pointer called TOP is used to keep track of the top element in the stack.
2. When initializing the stack, we set its value to -1 so that we can check if the stack is empty by comparing `TOP == -1`.
3. On pushing an element, we increase the value of TOP and place the new element in the position pointed to by TOP.
4. On popping an element, we return the element pointed to by TOP and reduce its value.
5. Before pushing, we check if the stack is already full
6. Before popping, we check if the stack is already empty

![stack](https://cdn.programiz.com/sites/tutorial2program/files/stack-operations.png)

### Implementation of Stack Data Structure
We can implement a stack in Python using a list. The list will act as the stack itself and the `append()` and `pop()` methods will be used to add and remove elements from the stack.

```python
class Stack:
    def __init__(self):
        self.stack = list()

    # check if the stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        # push element on the stack
        self.stack.append(data)

    # Use peek to look at the top of the stack
    def peek(self):
        return self.stack[-1]

    def pop(self):
        # pop element from the stack
        if self.isEmpty():
            return ("Stack is empty. Stack Underflow :(")
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def show(self):
        return self.stack

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.show())
print(s.pop())
print(s.show())
print(s.peek())
print(s.size())
```

### Output
```python
[1, 2, 3, 4]
4
[1, 2, 3]
3
3
```

### Applications of Stack Data Structure
Stacks are used in many applications. Some of them are:

- **Balancing of symbols:** In compilers, the parentheses, braces, and brackets are checked for their matching. This can be easily done using a stack.
- **Infix to Postfix Conversion:** In compilers, the infix expression is converted to postfix expression. This too can be done using a stack.
- **Undo mechanism in editors:** The undo mechanism in editors like Microsoft Word can be easily implemented using a stack.
- **Forward and backward feature in web browsers:** The forward and backward feature in web browsers store the history of visited pages. This too can be implemented using a stack.
- **Used in many algorithms like Tower of Hanoi, tree traversals, stock span problem, histogram problem.**