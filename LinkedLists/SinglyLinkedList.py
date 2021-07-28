class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    def search(self, key):
        index = 0
        curr = self.head
        if curr is None:
            return "Empty List"
        while curr is not None:
            if curr.data == key:
                return index
            index += 1
            curr = curr.next

    def delete(self, key):
        index = self.search(key)
        count = 0
        curr = self.head
        while count != index:
            prev = curr
            curr = curr.next
            count += 1
        if self.head is curr:
            self.head = curr.next
        else:
            prev.next = curr.next

    def maximum(self):
        maximum = 0
        curr = self.head
        while curr is not None:
            if curr.data > maximum:
                maximum = curr.data
            curr = curr.next
        return maximum

    def minimum(self):
        minimum = 100
        curr = self.head
        while curr is not None:
            if curr.data < minimum:
                minimum = curr.data
            curr = curr.next
        return minimum

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end='->')
            curr = curr.next


SLL = LinkedList()

SLL.prepend(1)
SLL.prepend(4)
SLL.prepend(7)
SLL.append(9)
SLL.prepend(6)

SLL.print_list()

print()

print("Maximum of this list is " + str(SLL.maximum()))

print("Minimium of this list is " + str(SLL.minimum()))
