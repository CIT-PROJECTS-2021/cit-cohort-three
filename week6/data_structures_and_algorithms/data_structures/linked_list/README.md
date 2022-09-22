# Linked list Data Structure

A linked list is a linear data structure that includes a series of connected nodes. Here, each node stores the data and the address of the next node. For example,

![Linked list data structure](https://cdn.programiz.com/sites/tutorial2program/files/linked-list-concept.png)


You have to start somewhere, so we give the address of the first node a special name called `HEAD`. Also, the last node in the linked list can be identified because its next portion points to NULL.

Linked lists can be of multiple types: singly, doubly, and circular linked list. In this article, we will focus on the singly linked list.

>**NOTE**: You might have played the game Treasure Hunt, where each clue includes the information about the next clue. That is how the linked list operates.

### Representation of Linked List
Let's see how each node of the linked list is represented. Each node consists:

- A data item
- An address of another node

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.print_list()
```

### Linked List Applications
Linked lists are used in many applications. Some of them are:

- Dynamic memory allocation
- Implemented in stack and queue
- In undo functionality of softwares
- Hash tables, Graphs