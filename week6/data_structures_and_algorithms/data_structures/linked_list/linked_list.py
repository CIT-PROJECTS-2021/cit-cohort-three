class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"data: {self.data} next -> : {self.next}"

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def size(self):
        temp = self.head
        print('temp: {}'.format(str(temp)))
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.print_list()
    print(f'size: {llist.size()}')



#    Node               Node
# [data|address] -> [data|address] -> Null