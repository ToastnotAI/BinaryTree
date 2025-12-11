import unittest
from BinaryTree import *

class TestBinaryTreeNode(unittest.TestCase):

    def test_import_node(self):
        try:
            from BinaryTree import Node
        except ImportError as e:
            self.fail(f"Importing Node failed with error: {e}")

    def test_node_initialization(self):
        node = Node(10)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 10) 
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_count_instances_of_value(self):
        node = Node(15)
        node.count += 1 # incrementing count attribute manually for testing
        self.assertEqual(node.count, 2)



class TestBinaryTree(unittest.TestCase):

    def test_import_binary_tree(self):
        try:
            from BinaryTree import BinaryTree
        except ImportError as e:
            self.fail(f"Importing BinaryTree failed with error: {e}")

    def test_tree_initialization(self):
        tree = BinaryTree()
        self.assertIsNotNone(tree)
        self.assertIsNone(tree.root)

    def test_add_root_node(self):
        tree = BinaryTree()
        tree.insert(Node(20))
        self.assertEqual(type(tree.root), Node)
        self.assertEqual(tree.root.value, 20)

    def test_add_single_left_child(self):
        tree = BinaryTree()
        tree.root = Node(30)
        left_child = Node(15)
        tree.insert(left_child)
        self.assertEqual(tree.root.left, left_child)
        self.assertLess(tree.root.left.value, tree.root.value)

    def test_add_single_right_child(self):
        tree = BinaryTree()
        tree.root = Node(30)
        right_child = Node(45)
        tree.insert(right_child)
        self.assertEqual(tree.root.right, right_child)
        self.assertGreater(tree.root.right.value, tree.root.value)
        
    def test_insert_multiple_nodes(self):
        tree = BinaryTree()
        tree.insert(Node(25))
        tree.insert(Node(10))
        tree.insert(Node(35))
        
        self.assertEqual(tree.root.value, 25)
        self.assertEqual(tree.root.left.value, 10)
        self.assertEqual(tree.root.right.value, 35)
    
    def test_insert_right_side_only(self):
        tree = BinaryTree()
        tree.insert(Node(5))
        tree.insert(Node(15))
        tree.insert(Node(25))

        self.assertEqual(tree.root.value, 5)
        self.assertEqual(tree.root.right.value, 15)
        self.assertEqual(tree.root.right.right.value, 25)
        self.assertEqual(tree.root.left, None)
        self.assertEqual(tree.root.right.left, None)

    def test_insert_left_side_only(self):
        tree = BinaryTree()
        tree.insert(Node(30))
        tree.insert(Node(20))
        tree.insert(Node(10))

        self.assertEqual(tree.root.value, 30)
        self.assertEqual(tree.root.left.value, 20)
        self.assertEqual(tree.root.left.left.value, 10)
        self.assertEqual(tree.root.right, None)
        self.assertEqual(tree.root.left.right, None)
    

    # This code was AI generated based on the function definition provided.
    def test_insert_mixed_nodes(self):
        tree = BinaryTree()
        values = [50, 30, 70, 20, 40, 60, 80]
        for val in values:
            tree.insert(Node(val))
        
        self.assertEqual(tree.root.value, 50)
        self.assertEqual(tree.root.left.value, 30) # 30 < 50
        self.assertEqual(tree.root.right.value, 70) #70 > 50
        self.assertEqual(tree.root.left.left.value, 20) #20 < 30 < 50
        self.assertEqual(tree.root.left.right.value, 40) #40 > 30 < 50
        self.assertEqual(tree.root.right.left.value, 60) #60 < 70 > 50
        self.assertEqual(tree.root.right.right.value, 80) #80 > 70 > 50


    # Duplicates utilise the count attribute of Node to track occurrences to reduce time complexity of tree.
    def test_insert_duplicate_values(self):
        tree = BinaryTree()
        tree.insert(Node(10))
        tree.insert(Node(10))

        self.assertEqual(tree.root.value, 10)
        self.assertIsNone(tree.root.left)
        self.assertIsNone(tree.root.right)
        self.assertEqual(tree.root.count, 2)

    def test_initialize_tree_with_list(self):
        values = [15, 10, 20, 5]
        tree = BinaryTree(values)
        self.assertEqual(tree.root.value, 15)
        self.assertEqual(tree.root.left.value, 10)
        self.assertEqual(tree.root.right.value, 20)
        self.assertEqual(tree.root.left.left.value, 5)

    def test_initialize_tree_with_empty_list(self):
        values = []
        tree = BinaryTree(values)
        self.assertIsNone(tree.root)

    def test_find_node_in_tree(self):
        values = [40, 20, 60, 10, 30, 50, 70]
        tree = BinaryTree(values)
        found = tree.find(30)
        not_found = tree.find(100)

        self.assertTrue(found)        
        self.assertFalse(not_found)

    def test_count_instances_of_value(self):
        tree = BinaryTree()
        tree.insert(Node(25))
        tree.insert(Node(25))
        tree.insert(Node(30))
        tree.insert(Node(25))

        self.assertEqual(tree.count(25), 3)
        self.assertEqual(tree.count(30), 1)
        self.assertEqual(tree.count(40), 0)

    def test_longest_path_one_node(self):
        tree = BinaryTree()
        tree.insert(Node(10))
        longest_path = tree.longest_path()
        self.assertEqual(longest_path, 1)  # Only root node

    def test_longest_path_in_tree(self):
        values = [50, 30, 70, 20, 40, 60, 80, 10]
        tree = BinaryTree(values)
        longest_path = tree.longest_path()
        self.assertEqual(longest_path, 4)  # Path: 50 -> 30 -> 20 -> 10

    def test_longest_path_empty_tree(self):
        tree = BinaryTree()
        longest_path = tree.longest_path()
        self.assertEqual(longest_path, 0)  # No nodes in the tree

    def test_longest_path_left_heavy_tree(self):
        values = [100, 90, 80, 70, 60]
        tree = BinaryTree(values)
        longest_path = tree.longest_path()
        self.assertEqual(longest_path, 5)  # Path: 100 -> 90 -> 80 -> 70 -> 60
    
    def test_longest_path_right_heavy_tree(self):
        values = [10, 20, 30, 40, 50]
        tree = BinaryTree(values)
        longest_path = tree.longest_path()
        self.assertEqual(longest_path, 5)  # Path: 10 -> 20 -> 30 -> 40 -> 50
    
        
