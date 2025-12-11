import unittest

class TestBinaryTree(unittest.TestCase):

    def test_import_binary_tree(self):
        try:
            from BinaryTree import BinaryTree
        except ImportError as e:
            self.fail(f"Importing BinaryTree failed with error: {e}")


class TestBinaryTreeNode(unittest.TestCase):

    def test_import_node(self):
        try:
            from BinaryTree import Node
        except ImportError as e:
            self.fail(f"Importing Node failed with error: {e}")
        
