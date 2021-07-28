class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def preOrderPrint(self, node):
        # recursively, visit the current node before it's children
        if node:
            print(str(node.data) + "->", end="")
            self.preOrderPrint(node.left)
            self.preOrderPrint(node.right)

    def inOrderPrint(self, node):
        # recursively, visit the left child, visit the current node, and then visit the right child
        if node:
            self.inOrderPrint(node.left)
            print(str(node.data) + "->", end="")
            self.inOrderPrint(node.right)

    def postOrderPrint(self, node):
        # recursively, visit the left child, visit the right child, and then visit the current node
        if node:
            self.postOrderPrint(node.left)
            self.postOrderPrint(node.right)
            print(str(node.data) + "->", end="")


BinaryTree = BinaryTree(1)
BinaryTree.root.left = Node(2)
BinaryTree.root.right = Node(3)
BinaryTree.root.left.left = Node(4)
BinaryTree.root.left.right = Node(5)
BinaryTree.root.right.left = Node(6)
BinaryTree.root.right.right = Node(7)

BinaryTree.preOrderPrint(BinaryTree.root)
print()
BinaryTree.inOrderPrint(BinaryTree.root)
print()
BinaryTree.postOrderPrint(BinaryTree.root)