class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = new_node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
            self.head = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def remove(self,key):
        if self.head:
            if self.head.data == key:
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head
                prev = None
                while cur.data != key:
                    prev = cur
                    cur = cur.next
                prev.next = cur.next

    def split_lists(self):
        if self.head:
            CLL2 = CircularLinkedList()
            length = 0
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
                length += 1
            if length == 0:
                print("Only one node")
                return
            count = 0
            cur = self.head
            while count != (length // 2):
                cur = cur.next
                count += 1
            CLL2.head = cur.next
            cur.next = self.head
            cur = CLL2.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = CLL2.head
            print("List 1:")
            self.print_list()
            print("List 2:")
            CLL2.print_list()


CLL = CircularLinkedList()
CLL.append("A")
CLL.append("B")
CLL.append("C")
CLL.append("D")
CLL.append("E")
CLL.append("F")

CLL.split_lists()
