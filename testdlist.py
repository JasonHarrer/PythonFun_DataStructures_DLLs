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


    def test_remove_at(self):
        dll = DList()
        test_nodes = []
        add_num_nodes = randint(3, 10)
        remove_num_nodes = randint(1, add_num_nodes)
        # Add in nodes to test with
        for i in range(add_num_nodes):
            name = random_name()
            test_nodes.append(name)
            dll.append(name)
        print('\nNodes Added.')
        self.assertEqual(dll.len(), len(test_nodes))

        # Now remove the number of nodes
        while remove_num_nodes > 0:
            remove_node = randint(0, len(test_nodes)-1)
            print(f'\nRemoving node #{remove_node} of {len(test_nodes)}/{dll.len()}')
            del test_nodes[remove_node]
            dll.remove_at(remove_node)
            remove_num_nodes -= 1
            print(f'Assert lengths are equal: {dll.len()} = {len(test_nodes)}')
            self.assertEqual(dll.len(), len(test_nodes))
        # Now validate that the two lists are the same
        self.assertEqual(dll.len(), len(test_nodes))
        runner = dll.head
        for i in range(len(test_nodes)):
            print(f'Assert value {runner.value} = {test_nodes[i]}')
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


    #def test_remove_duplicates(self):
    #    dll = DList()
    #    test_nodes = []
    #    num_test_nodes = randint(30, 50)  # Really high number to ensure we have duplicates
    #    # Load test nodes
    #    for i in range(num_test_nodes):
    #        name = random_name()
    #        dll.append(name)
    #        test_nodes.append(name)
    #    print('\nNodes added.')
    #    print('Assert lengths are equal')
    #    self.assertEqual(dll.len(), len(test_nodes))
    #    # Now remove duplicates, both from the test_nodes and the DList
    #    test_nodes = list(dict.fromkeys(test_nodes))
    #    dll.remove_duplicates()

    #    # Now validate that the two lists are the same
    #    print('\nNodes removed.')
    #    print('Assert lengths are equal')
    #    self.assertEqual(dll.len(), len(test_nodes))
    #    runner = dll.head
    #    for i in range(len(test_nodes)):
    #        self.assertEqual(runner.value, test_nodes[i])
    #        if i == 0:
    #            self.assertIsNone(runner.previous)
    #        else:
    #            self.assertEqual(runner.previous.value, test_nodes[i-1])
    #        if i == (len(test_nodes)-1):
    #            self.assertIsNone(runner.next)
    #        else:
    #            self.assertEqual(runner.next.value, test_nodes[i+1])
    #        runner = runner.next



if __name__ == '__main__':
    unittest.main()
