class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def search(self, item):
        if not self.is_empty():
            for i in range(len(self.items)):
                if self.items[i] == item:
                    return i


myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")
print(myStack.search("B"))


