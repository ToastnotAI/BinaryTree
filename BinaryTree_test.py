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
    



    

        
