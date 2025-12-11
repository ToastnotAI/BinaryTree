class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    
class BinaryTree:
    root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            if new_node.value < self.root.value:
                self.root.left = new_node
            else:
                self.root.right = new_node