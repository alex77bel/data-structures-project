import unittest
from src.queue import Node, Queue


class TestNode(unittest.TestCase):

    def setUp(self):
        self.node = Node('data1', None)

    def test_node_init(self):
        self.assertEqual(self.node.data, 'data1')
        self.assertEqual(self.node.next_node, None)


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_queue_init(self):
        self.assertEqual(self.queue.tail, None)
        self.assertEqual(self.queue.head, None)

    def test_enqueue_str_dequeue(self):
        self.assertEqual(str(self.queue), '')
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        self.assertEqual(str(self.queue), 'data1\ndata2\ndata3')
        self.assertEqual(self.queue.dequeue(), 'data1')
        self.assertEqual(self.queue.dequeue(), 'data2')
        self.assertEqual(self.queue.dequeue(), 'data3')
        self.assertEqual(self.queue.dequeue(), None)
