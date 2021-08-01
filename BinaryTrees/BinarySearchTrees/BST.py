class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, root, new_val):
        if new_val < root.data:
            if not root.left:
                root.left = Node(new_val)
            else:
                self.insert(root.left, new_val)

        elif new_val > root.data:
            if not root.right:
                root.right = Node(new_val)
            else:
                self.insert(root.right, new_val)

    def search(self, root, value):
        # Base Case if node not found
        if root is None:
            return False
        # Base Case if node is found
        if value == root.data:
            return True
        else:
            if value < root.data:
                return self.search(root.left, value)
            else:
                return self.search(root.right, value)

    def inOrderPrint(self, root):
        if root:
            self.inOrderPrint(root.left)
            print(str(root.data) + "->", end="")
            self.inOrderPrint(root.right)

    def find_minimum(self, root):
        while root.left:
            root = root.left
        return root

    def find_maximum(self, root):
        while root.right:
            root = root.right
        return root

    def delete(self, root, value):
        if root is None:
            return root

        if value < root.data:
            root.left = self.delete(root.left, value)

        elif value > root.data:
            root.right = self.delete(root.right, value)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.find_minimum(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root


BST = BinarySearchTree(8)

BST.insert(BST.root, 3)
BST.insert(BST.root, 10)
BST.insert(BST.root, 1)
BST.insert(BST.root, 6)
BST.insert(BST.root, 4)
BST.insert(BST.root, 7)
BST.insert(BST.root, 14)
BST.insert(BST.root, 13)

BST.inOrderPrint(BST.root)

print()

print(BST.search(BST.root, 9))

print(BST.find_minimum(BST.root).data)

print(BST.find_maximum(BST.root).data)

BST.delete(BST.root, 14)

BST.inOrderPrint(BST.root)