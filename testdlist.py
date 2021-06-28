#!/usr/bin/env python

from random import randint
import unittest
from dlist import Node, DList

names = [ 'Alice', 'Bob', 'Cindy', 'Darren', 'Elaine', 'Francois', 'Georgia', 'Harold', 'Iris', 'Jordan', 'Kacey', 'Larry', 'Maureen', 
          'Norman', 'Olivia', 'Patrick', 'Queeny', 'Richard', 'Sharon', 'Terrence', 'Ursula', 'Victor', 'Wendy', 'Xavier', 'Yolanda','Zachary' ]


def random_name():
    return names[randint(0, len(names)-1)]


class TestDLL(unittest.TestCase):
    def test_append_one_node(self):
        dll = DList()
        name = random_name()
        new_node = Node(name)
        dll.append(name)
        self.assertEqual(dll.head.value, new_node.value)
        self.assertIsNone(dll.head.next)
        self.assertIsNone(dll.head.previous)

    def test_append_multiple_nodes(self):
        dll = DList()
        test_nodes = []
        num_nodes = randint(3, 10)
        for i in range(num_nodes):
            name = random_name()
            test_nodes.append(name)
            dll.push(name)          # synonymous with append
        self.assertEqual(dll.len(), num_nodes)
        runner = dll.head
        for i in range(num_nodes):
            self.assertEqual(runner.value, test_nodes[i])
            if i == 0:
                self.assertIsNone(runner.previous)
            else:
                self.assertEqual(runner.previous.value, test_nodes[i-1])
            if i == (num_nodes - 1):
                self.assertIsNone(runner.next)
            else:
                self.assertEqual(runner.next.value, test_nodes[i+1])
            runner = runner.next

    def test_prepend_one_node(self):
        dll = DList()
        name = random_name()
        new_node = Node(name)
        dll.prepend(name)
        self.assertEqual(dll.head.value, new_node.value)
        self.assertIsNone(dll.head.next)
        self.assertIsNone(dll.head.previous)


    def test_prepend_multiple_nodes(self):
        dll = DList()
        test_nodes = []
        num_nodes = randint(3, 10)
        for i in range(num_nodes):
            name = random_name()
            test_nodes.append(name)
            dll.prepend(name)
        self.assertEqual(dll.len(), len(test_nodes))
        runner = dll.head
        # Go backwards through range, as we prepended, so values will be backwards
        for i in range(len(test_nodes)):
            self.assertEqual(runner.value, test_nodes[(len(test_nodes)-1-i)])
            if i == 0:
                self.assertIsNone(runner.previous)
            else:
                self.assertEqual(runner.previous.value, test_nodes[(len(test_nodes)-i)])
            if i == (num_nodes - 1):
                self.assertIsNone(runner.next)
            else:
                self.assertEqual(runner.next.value, test_nodes[len(test_nodes)-2-i])
            runner = runner.next


    def test_insert_at(self):
        dll = DList()
        test_nodes = []
        num_nodes = 3
        for i in range(num_nodes):
            name = random_name()
            test_nodes.append(name)
            dll.append(name)

        num_tests = randint(3, 10)
        for i in range(num_tests):
            insert_name = random_name()
            insert_pos = randint(0, len(test_nodes)-1)
            dll.insert_at(insert_name, insert_pos)
            test_nodes.insert(insert_pos, insert_name)
        self.assertEqual(dll.len(), len(test_nodes))
        runner = dll.head
        for i in range(len(test_nodes)):
            self.assertEqual(runner.value, test_nodes[i])
            if i == 0:
                self.assertIsNone(runner.previous)
            else:
                self.assertEqual(runner.previous.value, test_nodes[i-1])
            if i == (len(test_nodes)-1):
                self.assertIsNone(runner.next)
            else:
                self.assertEqual(runner.next.value, test_nodes[i+1])
            runner = runner.next


if __name__ == '__main__':
    unittest.main()
