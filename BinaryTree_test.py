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
        tree= BinaryTree()
        tree.root = Node(30)
        left_child = Node(15)
        tree.insert(left_child)
        self.assertEqual(tree.root.left, left_child)


    

        
