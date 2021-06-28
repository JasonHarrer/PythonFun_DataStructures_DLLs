# ddl.py:  Doubly Linked List implementation

from enum import Enum

#class ResultType(Enum):
#    OK = 1
#    Error = 2
#
#class Result:
#    def __init__(self, return_type, value):
#        self.type = return_type
#        self.value = value
#        self.errors = []
#
#    def isError(self):
#        return True if self.type == ResultType.Error else False
#
#    def isOK(self):
#        return True if self.type == ResultType.OK else False
#
#    def getErrorMessages(self):
#        return self.errors
#
#    def getValue(self):
#        return self.value if self.type == ResultType.OK else None


class Node:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous

    def __str__(self):
        return f'Node: {self.value}'


class DList:
    def __init__(self):
        self.head = None


    def __str__(self):
        rep = '{ '
        runner = self.head
        while runner is not None:
            rep += runner.value
            if runner.next is not None:
                rep += ', '
            runner = runner.next
        rep += ' }'
        return rep


    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        new_node.previous = None
        if self.head is not None:
            self.head.previous = new_node
        self.head = new_node
        return self


    def append(self, value):
        new_node = Node(value)
        runner = self.head
        if runner is not None:
            while runner.next is not None:
                runner = runner.next
            new_node.previous = runner
            new_node.next = None
            runner.next = new_node
        else:
            self.head = new_node
        return self


    def push(self, value):
        self.append(value)

    def insert_at(self, value, pos):
        if pos > self.len():
            print(f'Error: Position {pos} is outside the bounds of the Doubly Linked List.')
            return self

        if pos == 0:
            self.prepend(value)
        elif pos == self.len():
            self.append(value)
        else:
            new_node = Node(value)
            runner = self.head
            node_counter = 0
            while node_counter != pos and runner is not None:
                node_counter += 1
                runner = runner.next
            new_node.previous = runner.previous
            new_node.previous.next = new_node
            new_node.next = runner
            runner.previous = new_node
        return self
            

    def remove_at(self, value, pos):
        pass


    def value(self, pos):
        if pos > self.len():
            print(f'Error: Position {pos} is outside the bounds of the Doubly Linked List.')
            return None 
        runner = self.head
        counter = 0
        while counter != pos and runner is not None:
            counter += 1
            runner = runner.next
        return runner.value


    def len(self):
        counter = 0
        runner = self.head
        while runner is not None:
            runner = runner.next
            counter += 1
        return counter

    def remove_duplicates(self):
        pass

    def is_circular_list(self):
        pass

    def reverse(self):
        pass
