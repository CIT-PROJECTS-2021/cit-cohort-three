# Queue Data Structure
In this lecture, you will learn what a queue is. Also, you will find implementation of queue in Python.

A queue is a useful data structure in programming. It is similar to the ticket queue outside a cinema hall, where the first person entering the queue is the first person who gets the ticket.

Queue follows the First In First Out (FIFO) rule - the item that goes in first is the item that comes out first.

![queue](https://cdn.programiz.com/sites/tutorial2program/files/queue.png)

In the above image, since 1 was kept in the queue before 2, it is the first to be removed from the queue as well. It follows the FIFO rule.

In programming terms, putting items in the queue is called enqueue, and removing items from the queue is called dequeue.

We can implement the queue in any programming language like C, C++, Java, Python or C#, but the specification is pretty much the same.

**

### Basic Operations of Queue
A queue is an object (an abstract data structure - ADT) that allows the following operations:

- **Enqueue:** Add an element to the end of the queue
- **Dequeue:** Remove an element from the front of the queue
- **IsEmpty:** Check if the queue is empty
- **IsFull:** Check if the queue is full
- **Peek:** Get the value of the front of the queue without removing it

### Working of Queue
Queue operations work as follows:

- two pointers `FRONT` and `REAR`
- `FRONT` track the first element of the queue
- `REAR` track the last element of the queue
- initially, set value of `FRONT` and `REAR` to `-1`

### Enqueue Operation
- check if the queue is full
- for the first element, set the value of `FRONT` to 0
- increase the `REAR` index by 1
- add the new element in the position pointed to by `REAR`

### Dequeue Operation
- check if the queue is empty
- return the value pointed by `FRONT`
- increase the `FRONT` index by `1`
- for the last element, reset the values of `FRONT` and `REAR` to `-1`

![queue](https://cdn.programiz.com/sites/tutorial2program/files/Queue-program-enqueue-dequeue.png)


### Implementation of Queue in Python
We can implement a queue in Python using a list. The list will act as the queue itself and the `append()` and `pop()` methods will be used to add and remove elements from the queue.

```python
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
```

### Limitations of Queue
As you can see in the image below, after a bit of enqueuing and dequeuing, the size of the queue has been reduced.

![queue](https://cdn.programiz.com/sites/tutorial2program/files/why-circular-queue_0.png)

And we can only add indexes 0 and 1 only when the queue is reset (when all the elements have been dequeued).

After REAR reaches the last index, if we can store extra elements in the empty spaces (0 and 1), we can make use of the empty spaces. This is implemented by a modified queue called the circular queue.

### Application of Queue
- **CPU Scheduling:** In operating systems, the task scheduler uses a queue to store the list of tasks that are waiting to be executed.
- **Handling of interrupts in real-time systems:** The interrupts are handled in the same order as they arrive, which is handled by a queue.
- **Call Center phone systems:** The phone systems use a queue to hold people calling them in an order, until a service representative is free.
- **Data transfer:** Data transfer is done in the same order as they arrive, which is handled by a queue.
- **Buffer:** A buffer is a temporary storage area. A common example is the memory that is used to store data while it is being transferred from one place to another. It is often implemented as a queue.
- **Printing:** Print jobs are stored in a queue, and the printer prints them in the order they were received.
- **Traffic light:** The traffic light changes in the order red -> green -> yellow, which is handled by a queue.

### Recommended Readings
- Types of Queue
- Circular Queue
- Deque Data Structure
- Priority Queue