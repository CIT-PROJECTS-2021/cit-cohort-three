# Data Structure and Types

### What are Data Structures?
Data structure is a storage that is used to store and organize data. It is a way of arranging data on a computer so that it can be accessed and updated efficiently.

Depending on your requirement and project, it is important to choose the right data structure for your project. For example, if you want to store data sequentially in the memory, then you can go for the Array data structure.

<img src="https://cdn.programiz.com/cdn/farfuture/xl3N_KXHJEeqp83aLDgy9mO6yAKNM93I_rTfJXz8I0Q/mtime:1623152250/sites/tutorial2program/files/array_dsa.png" alt="Array data Structure Representation">

> **NOTE**: Note: Data structure and data types are slightly different. Data structure is the collection of data types arranged in a specific order.

### Types of Data Structures
Basically, data structures are divided into two categories:

- Linear Data Structures
- Non-Linear Data Structures

#### Linear Data Structures
Linear data structures are those data structures in which data elements are arranged in a sequential manner. In other words, we can say that the elements are arranged in a linear order. The elements are linked using pointers.

In linear data structures, the elements are arranged in sequence one after the other. Since elements are arranged in particular order, they are easy to implement.

However, when the complexity of the program increases, the linear data structures might not be the best choice because of operational complexities.

Some of the linear data structures are:

### 1. Array Data Structure
In an array, elements in memory are arranged in continuous memory. All the elements of an array are of the same type. And, the type of elements that can be stored in the form of arrays is determined by the programming language.

<img src="https://cdn.programiz.com/cdn/farfuture/CvSYKIrQaK-KlCU2PC0qZULI9kZa33XK3-HH1uipQIE/mtime:1623152231/sites/tutorial2program/files/array_.png" alt="An array">

> **NOTE**: Note: The elements of an array are stored in a contiguous memory location. The first element of the array is stored at the lowest memory address. The last element of the array is stored at the highest memory address.

### 2. Stack Data Structure
In stack data structure, elements are stored in the LIFO principle. That is, the last element stored in a stack will be removed first.

It works just like a pile of plates where the last plate kept on the pile will be removed first.

<img src="https://cdn.programiz.com/cdn/farfuture/kDcDcLDytJ7-aLU-7zVQAIiMLfh4TOvi-mZR10hOCFg/mtime:1623152242/sites/tutorial2program/files/stack_dsa.png" alt="stack">

> **NOTE**: Note: The stack is a linear data structure that follows the LIFO principle. The last element inserted in the stack will be removed first.

### 3. Queue Data Structure
Unlike stack, the queue data structure works in the FIFO principle where first element stored in the queue will be removed first.

It works just like a queue of people in the ticket counter where first person on the queue will get the ticket first. 

<img src="https://cdn.programiz.com/cdn/farfuture/Li6chlo-utkw-FHPvLC_IiManoc41y1yEpUzwkj8iY8/mtime:1623152237/sites/tutorial2program/files/queue_dsa.png" alt="queue">

> **NOTE**: Note: The queue is a linear data structure that follows the FIFO principle. The first element inserted in the queue will be removed first.

### 4. Linked List Data Structure
In linked list data structure, data elements are connected through a series of nodes. And, each node contains the data items and address to the next node.

<img src="https://cdn.programiz.com/cdn/farfuture/m9VXEfUlR739aTq0OmxoCW3z5sgKYuMLajEmP-q3J88/mtime:1623152210/sites/tutorial2program/files/linked-list_dsa.png" alt="linked list">

> **NOTE**: Note: The linked list is a linear data structure that contains a sequence of nodes. Each node contains a data item and a pointer to the next node.

### Non linear data structures
Unlike linear data structures, elements in non-linear data structures are not in any sequence. Instead they are arranged in a hierarchical manner where one element will be connected to one or more elements.

Non-linear data structures are further divided into graph and tree based data structures.

### 1. Graph Data Structure
In graph data structure, each node is called vertex and each vertex is connected to other vertices through edges. The edges are used to represent the relationship between the vertices.

<img src="https://cdn.programiz.com/cdn/farfuture/9QtvaweNfvWiBsAgt81aNynEhJXovky4lCoFgyU_Y-0/mtime:1623152219/sites/tutorial2program/files/graph_dsa.png">

> **NOTE**: Note: The graph is a non-linear data structure that consists of a finite set of vertices and edges. Each edge connects two vertices.

### 2. Tree Data Structure
Similar to a graph, a tree is also a collection of vertices and edges. However, in tree data structure, there can only be one edge between two vertices.

<img src="https://cdn.programiz.com/cdn/farfuture/oJBsOWQ4sBd6DYjtaDq4MtU2fIxMWfuD-eMU0ePauIE/mtime:1623152223/sites/tutorial2program/files/tree_dsa.png">

> **NOTE**: Note: The tree is a non-linear data structure that consists of a finite set of nodes and edges. Each edge connects two nodes.

### Linear Vs Non-linear Data Structures
Now that we know about linear and non-linear data structures, let's see the major differences between them.

| Linear Data Structures | Non-linear Data Structures |
| --- | --- |
| Elements are arranged in a sequential manner. | Elements are arranged in a hierarchical manner. |
| Elements are connected using pointers. | Elements are connected using pointers. |
| The elements are easy to implement. | The elements are difficult to implement. |
|It can be traversed on a single run. That is, if we start from the first element, we can traverse all the elements sequentially in a single pass.| t requires multiple runs. That is, if we start from the first element it might not be possible to traverse all the elements in a single pass.
| The complexity of the program increases. | The complexity of the program decreases. |
| Examples: Array, Stack, Queue, Linked List | Examples: Graph, Tree |

### Why Data Structure?
Knowledge about data structures help you understand the working of each data structure. And, based on that you can select the right data structures for your project.

This helps you write memory and time efficient code.
