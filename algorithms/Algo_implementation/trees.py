class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


# TEST CONSTRUCTOR
my_tree = BinarySearchTree()

print("Root:", my_tree.root)
