import unittest
from src.linked_list import Node, LinkedList


class TestNode(unittest.TestCase):

    def setUp(self):
        self.node = Node({'id': 1}, None)

    def test_node_init(self):
        self.assertEqual(self.node.data, {'id': 1})
        self.assertEqual(self.node.next_node, None)


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.LinkedList = LinkedList()

    def test_LinkedList_init(self):
        self.assertEqual(self.LinkedList.tail, None)
        self.assertEqual(self.LinkedList.head, None)

    def test_enLinkedList_str_insert_beginning_insert_at_end(self):
        self.LinkedList.insert_beginning({'id': 1})
        self.assertEqual(self.LinkedList.head.data, {'id': 1})
        self.LinkedList.insert_at_end({'id': 2})
        self.assertEqual(self.LinkedList.tail.data, {'id': 2})
        self.LinkedList.insert_at_end({'id': 3})
        self.assertEqual(self.LinkedList.tail.data, {'id': 3})
        self.LinkedList.insert_beginning({'id': 0})
        self.assertEqual(self.LinkedList.head.data, {'id': 0})
        assert str(self.LinkedList) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"


    def test_to_list(self):
        self.LinkedList.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.LinkedList.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.LinkedList.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.LinkedList.insert_beginning({'id': 0, 'username': 'serebro'})
        lst = self.LinkedList.to_list()
        self.assertEqual(lst,[{'id': 0, 'username': 'serebro'},
                              {'id': 1, 'username': 'lazzy508509'},
                              {'id': 2, 'username': 'mik.roz'},
                              {'id': 3, 'username': 'mosh_s'}])

    def test_get_data_by_id(self):
        self.LinkedList.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.LinkedList.insert_at_end('idusername')
        self.LinkedList.insert_at_end([1, 2, 3])
        self.LinkedList.insert_at_end({'id': 2, 'username': 'mosh_s'})
        user_data = self.LinkedList.get_data_by_id(2)
        self.assertEqual(user_data, {'id': 2, 'username': 'mosh_s'})