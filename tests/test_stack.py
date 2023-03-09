import unittest
from src.stack import Node, Stack


class TestNode(unittest.TestCase):

    def setUp(self):
        self.node = Node(5, None)

    def test_node_init(self):
        self.assertEqual(self.node.data, 5)
        self.assertEqual(self.node.next_node, None)


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_stack_init(self):
        self.assertEqual(self.stack.nodes, [])

    def test_stack_top(self):
        self.assertEqual(self.stack.top(), None)
