class Queue:
    def __init__(self):
        self.queue = list()

    # check if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # add an element to the queue
    def enqueue(self, data):
        # insert method to add element
        self.queue.insert(0, data)
        # [2, 8, 5, 4]
        return True

    # remove an element from the queue
    def dequeue(self):
        if self.isEmpty():
            return ("Queue is empty!")
        return self.queue.pop()

    # get the size of the queue
    def size(self):
        return len(self.queue)

    # display the queue
    def display(self):
        return self.queue

# create a Queue object
q = Queue()

# insert elements to the queue
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)

# display the queue
print(q.display())

# remove an element from the queue
print(q.dequeue())

# display the queue
print(q.display())

# check the size of the queue
print(q.size())

# check if the queue is empty
print(q.isEmpty())


class AnotherQueue:
    def __init__(self):
        self.queue = list()

    # [1, 2, 3, 4, 5, 6]

    # check if empty
    def isEmpty(self):
        return len(self.queue) == 0

    # enqueue
    def enqueue(self, data):
        self.queue.append(data)

    # dequeue
    def dequeue(self):
        if self.isEmpty():
            return "Queu is empty"

        return self.queue.pop(0)

    def display(self):
        return self.queue



s = AnotherQueue()
print(s.dequeue())
s.enqueue('data')
s.enqueue('another data')
print(s.display())
print(s.dequeue())
print(s.display())



