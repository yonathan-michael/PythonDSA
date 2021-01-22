class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
        else:
            self.head = new_node

    def prepend(self, data):
        if self.head:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.append(data)

    def print_list(self):
        if self.head:
            curr = self.head
            while curr:
                print(curr.data)
                curr = curr.next
        else:
            print("List is empty")

    def add_node_after(self, key, data):
        cur = self.head
        while cur:
            if cur.data == key and cur.next is None:
                self.append(data)
                return
            elif cur.data == key:
                new_Node = Node(data)
                new_Node_next = cur.next
                cur.next.prev = new_Node
                cur.next = new_Node
                new_Node.next = new_Node_next
                new_Node.prev = cur
                return
            cur = cur.next

    def add_node_before(self, key, data):
        cur = self.head
        while cur:
            if cur.data == key and cur.prev is None:
                self.prepend(data)
                return
            elif cur.data == key:
                new_Node = Node(data)
                new_Node.next = cur
                prev = cur.prev
                cur.prev = new_Node
                prev.next = new_Node
                new_Node.prev = prev
                return
            cur = cur.next


DLL = DoublyLinkedList()

DLL.append("A")
DLL.append("B")
DLL.append("C")

# DLL.add_node_after("B", "D")
DLL.add_node_before("C", "D")

DLL.print_list()
