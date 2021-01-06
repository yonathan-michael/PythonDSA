class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def append_after(self, data, prev_data):
        new_node = Node(data)

        prev_node = self.head

        while prev_node.data is not prev_data:
            prev_node = prev_node.next
            if prev_node is None:
                return

        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):

        curr_node = self.head

        while curr_node:
            print(curr_node.data, "->", end=" ")
            curr_node = curr_node.next


SLL = LinkedList()
SLL.append("A")
SLL.append("B")
SLL.prepend("C")
SLL.append_after("X", "C")
SLL.insert_after_node(SLL.head.next, "Z")

SLL.print_list()
