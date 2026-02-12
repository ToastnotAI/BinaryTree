import networkx

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

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root


    def get_balance_factor(self, currentNode):
        if currentNode is None:
            return 0
        leftDepth = self.longest_path_recursive(currentNode.left)
        rightDepth = self.longest_path_recursive(currentNode.right)
        return leftDepth - rightDepth
            
    def balance_tree_recursive(self, currentNode):
        if currentNode is None:
            return None
        
        # Recursively balance children first (bottom-up)
        currentNode.left = self.balance_tree_recursive(currentNode.left)
        currentNode.right = self.balance_tree_recursive(currentNode.right)
        
        balance_factor = self.get_balance_factor(currentNode)

        # Left heavy
        if balance_factor > 1:
            # Left-Right case
            if self.get_balance_factor(currentNode.left) < 0:
                currentNode.left = self.rotate_left(currentNode.left)
            # Left-Left case
            return self.rotate_right(currentNode)

        # Right heavy
        elif balance_factor < -1:
            # Right-Left case
            if self.get_balance_factor(currentNode.right) > 0:
                currentNode.right = self.rotate_right(currentNode.right)
            # Right-Right case
            return self.rotate_left(currentNode)

        return currentNode

    def balance_tree(self, currentNode=None):
        if currentNode == None:
            currentNode = self.root

        currentNode = self.balance_tree_recursive(currentNode)
        self.root = currentNode
        if abs(self.get_balance_factor(currentNode)) > 1:
            self.balance_tree(currentNode)



    def insert_recursive(self, currentNode, newNode):
        #duplicate nodes increment the count of the node already in the tree
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
        
    def find_recursive(self, currentNode, value):
        if currentNode is None:
            return False
        
        if currentNode.value == value:
            return currentNode
        
        elif value < currentNode.value:
            return self.find_recursive(currentNode.left, value)
        else:
            return self.find_recursive(currentNode.right, value)

        
    def find(self, value):
        return self.find_recursive(self.root, value)

    
    def count(self, value):
        return self.count_recursive(self.root, value)

    def longest_path_recursive(self, currentNode):
        if currentNode is None:
            return 0

        leftDepth = self.longest_path_recursive(currentNode.left)
        rightDepth = self.longest_path_recursive(currentNode.right)
        return 1 + max(leftDepth, rightDepth)

    def longest_path(self):
        return self.longest_path_recursive(self.root)

    def __repr__(self):
        if self.root is None:
            return "BinaryTree(empty)"

        G = networkx.DiGraph()

        def add_nodes_edges(node, pos=None, x=0, y=0, layer=1):
            if node is None:
                return pos
            
            if pos is None:
                pos = {}
            
            pos[id(node)] = (x, y)
            G.add_node(id(node), label=f"{node.value}\n({node.count})")
            
            dx = 1 / (2 ** layer)
            
            if node.left is not None:
                G.add_edge(id(node), id(node.left))
                add_nodes_edges(node.left, pos, x - dx, y - 1, layer + 1)
            
            if node.right is not None:
                G.add_edge(id(node), id(node.right))
                add_nodes_edges(node.right, pos, x + dx, y - 1, layer + 1)
            
            return pos

        pos = add_nodes_edges(self.root)

        import matplotlib.pyplot as plt
        plt.figure(figsize=(12, 8))
        labels = networkx.get_node_attributes(G, 'label')
        networkx.draw(G, pos, labels=labels, with_labels=True, 
                      node_color='lightblue', node_size=1500, 
                      font_size=10, font_weight='bold', 
                      arrows=True, arrowsize=20)
        plt.title("Binary Tree Structure")
        plt.show()

        return f"BinaryTree(nodes={G.number_of_nodes()}, depth={self.longest_path()})"


if __name__ == "__main__":
    import random
    import time
    def timeFunction(func, *args):
        startTime = time.time()
        result = func(*args)
        endTime = time.time()
        return result, endTime - startTime

    totalValues = 10
    values = [random.randint(1, 10000000) for _ in range(totalValues)]
    tree, timeTaken = timeFunction(BinaryTree, values)
    print(f"Inserted {totalValues} values into the BinaryTree in {timeTaken:.6f} seconds.")
    longestPath, timeTaken = timeFunction(tree.longest_path)
    print(f"Longest path in the tree is {longestPath}. Computed in {timeTaken:.8f} seconds.")
    sampleValue =values[random.randint(0, totalValues - 1)]
    print("Sample value to count:", sampleValue)
    countOf, timeTaken = timeFunction(tree.count, sampleValue)
    print(f"Count of value {sampleValue} in the tree is {countOf}. Computed in {timeTaken:.8f} seconds.")
    x, timeTaken = timeFunction(tree.count, 99999)
    print(f"Count of value 99999 in the tree is {x}. Computed in {timeTaken:.8f} seconds.")

    print(tree)


