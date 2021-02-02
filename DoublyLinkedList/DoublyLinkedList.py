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

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # Case 1
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                # Case 2
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            elif cur.data == key:
                # Case 3
                if not cur.next:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    prev = cur.prev
                    nxt = cur.next
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur = None
                    self.head = None
                    return

                # Case 2:
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur == node:
                # Case 3:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return

                # Case 4:
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def reverse(self):
        cur = self.head
        while cur.next:
            prev = cur.prev
            nxt = cur.next
            cur.next = prev
            cur.prev = nxt
            cur = nxt
        prev = cur.prev
        cur.next = prev
        cur.prev = None
        self.head = cur

    def remove_duplicates(self):
        cur = self.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt

    def pairs_with_sums(self, sum_val):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
                q = q.next
            p = p.next
        return pairs


DLL = DoublyLinkedList()

DLL.append(1)
DLL.append(2)
DLL.append(3)
DLL.append(4)
DLL.append(5)

DLL.print_list()

print(DLL.pairs_with_sums(9))
