class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1
    
    
class BinaryTree:
    root = None

    def __init__(self, values=None):
        if values is not None:
            for value in values:
                self.insert(Node(value))

        else:
            self.root = None

    def insert_recursive(self, currentNode, newNode):
        if currentNode.value == newNode.value:
            currentNode.count += 1
        
        elif newNode.value < currentNode.value:
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

    def count_recursive(self, currentNode, value):
        if currentNode is None:
            return 0

        if currentNode.value == value:
            return currentNode.count
        
        elif value < currentNode.value:
            return self.count_recursive(currentNode.left, value)
        
        else:
            return self.count_recursive(currentNode.right, value)

        
    def find(self, value):
        currentNode = self.root
        return (self.count_recursive(currentNode, value) > 0)
    
    def count(self, value):
        return self.count_recursive(self.root, value)

    def longest_path_recursive(self, currentNode, currentDepth):
        if currentNode is None:
            return currentDepth - 1
        
        leftDepth = self.longest_path_recursive(currentNode.left, currentDepth + 1)
        rightDepth = self.longest_path_recursive(currentNode.right, currentDepth + 1)
        return max(leftDepth, rightDepth)

    def longest_path(self):
        return self.longest_path_recursive(self.root, 1)


if __name__ == "__main__":
    import random
    import time
    totalValues = 5000
    values = [random.randint(1, 10000) for _ in range(totalValues)]
    startTime = time.time()
    tree = BinaryTree(values)
    endTime = time.time()
    print(f"Inserted {totalValues} values into the BinaryTree in {endTime - startTime:.6f} seconds.")
    print("Longest path in the tree:", tree.longest_path())
    sampleValue = values[random.randint(0, totalValues - 1)]
    print("Sample value to count:", sampleValue)
    print(f"Count of value {sampleValue} in the tree:", tree.count(sampleValue))
    print("Finding value 99999 in the tree:", tree.find(99999))
    print(f"Count of value 99999 in the tree:", tree.count(99999))


