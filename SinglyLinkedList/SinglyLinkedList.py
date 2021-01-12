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

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        else:
            while cur_node:
                prev_node = cur_node
                cur_node = cur_node.next
                if cur_node.data == key:
                    prev_node.next = cur_node.next
                    cur_node = None
                    return
        print("No node with this value")

    def delete_node_at_position(self, position):
        if self.head:
            cur_node = self.head
            if position == 0:
                self.head = cur_node.next
                cur_node = None
                return

            prev = None
            count = 0

            while cur_node and count != position:
                prev = cur_node
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return

            prev.next = cur_node.next
            cur_node = None

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return

        prev1 = None
        curr1 = self.head

        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head

        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            return

        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next = curr2.next
        curr2.next = curr1.next

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):

        curr_node = self.head

        while curr_node:
            print(curr_node.data, "->", end=" ")
            curr_node = curr_node.next

    def len_iterative(self):
        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.len_recursive(node.next)

    def reverse_iterative(self):
        cur = self.head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = {}

        while cur:
            if cur.data in dup_values:
                prev.next = cur.next
                cur = None
            else:
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def print_nth_from_last(self, n):
        total_len = self.len_iterative()
        cur = self.head
        while cur:
            if n == total_len:
                print(cur.data)
                return cur.data
            cur = cur.next
            total_len -= 1
        if cur is None:
            return

    def count_occurences_iterative(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None


SLL = LinkedList()
SLL2 = LinkedList()

SLL.append(1)
SLL.append(3)
SLL.append(3)

SLL2.append(2)
SLL2.append(4)

print("List 1")
SLL.print_list()
print(SLL.len_recursive(SLL.head))
print()
print("Let's Reverse")
SLL.reverse_iterative()
SLL.print_list()
print(SLL.len_recursive(SLL.head))
print()

print("List 2")
SLL2.print_list()
print(SLL2.len_iterative())
print()
print("Let's Reverse")
SLL2.reverse_recursive()
SLL2.print_list()
print(SLL.len_recursive(SLL2.head))

# Reverse Back
SLL.reverse_iterative()
SLL2.reverse_recursive()

print()
print("Let's merge:")
SLL.merge_sorted(SLL2)
SLL.print_list()
print()

