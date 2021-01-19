from SinglyLinkedList.SinglyLinkedList import LinkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        curr = self.head
        count = 1
        if self.head:
            while curr.next != self.head:
                curr = curr.next
                count += 1
            return count
        else:
            return 0

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

    def remove(self, key):
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

    def remove_node(self, node):
        if self.head == node:
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
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(self, step):
        cur = self.head

        while len(self) > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            print("KILL:" + str(cur.data))
            self.remove_node(cur)
            cur = cur.next

    def is_Circular(self, input_list):
        cur = input_list.head
        while cur.next != input_list.head:
            if cur.next is None:
                return False
            cur = cur.next
        return True


llist = LinkedList()
llist.append("A")
llist.append("B")

CLL = CircularLinkedList()
CLL.append("A")
print(CLL.is_Circular(llist))
print(CLL.is_Circular(CLL))
