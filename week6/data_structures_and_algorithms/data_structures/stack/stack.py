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


if __name__ == '__main__':
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
    s.push('Hello')
    s.push('data')
    print(s.show())
    print(s.peek())
    print(s.pop())
    print(s.show())
