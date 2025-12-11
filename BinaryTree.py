class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    
class BinaryTree:
    root = None

    def insert_recursive(self, currentNode, newNode):
        if newNode.value < currentNode.value:
            if currentNode.left is None:
                currentNode.left = newNode
            else:
                self.insert_recursive(currentNode.left, newNode)
        
        else:
            if currentNode.right is None:
                currentNode.right = newNode
            else:
                self.insert_recursive(currentNode.right, newNode)
                
    def insert(self, newNode):
        if self.root is None:
            self.root = newNode
        else:
            self.insert_recursive(self.root, newNode)