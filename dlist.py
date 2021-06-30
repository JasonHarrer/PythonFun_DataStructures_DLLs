# ddl.py:  Doubly Linked List implementation


class Node:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous

    def __str__(self):
        return_string = f'Node: {self.value}'.ljust(20)
        if self.previous is None:
            return_string += '\tPrevious: None'.ljust(20)
        else:
            return_string += f'\tPrevious: {self.previous.value}'.ljust(20)
        if self.next is None:
            return_string += '\tNext: None'
        else:
            return_string += f'\tNext: {self.next.value}'
        return return_string


class DList:
    def __init__(self):
        self.head = None


    def __str__(self):
        rep = '{'
        runner = self.head
        while runner is not None:
            rep += f'\n\t{runner}'
            if runner.next is not None:
                rep += ', '
            runner = runner.next
        rep += '\n}'
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
            

    def remove_at(self, pos):
        if pos >= self.len():
            print(f'Error: Position {pos} is outside the bounds of the Doubly Linked List.')
            return self
        i = 0
        runner = self.head
        while i < pos and runner is not None:
            runner = runner.next
            i += 1
        print(f'\ni = {i} of {self.len()-1}, pos = {pos} and runner = {runner}')
        print(f'\nRemoving Node {runner}')
        if runner.previous is not None:
            print('runner.previous is not None')
            runner.previous.next = runner.next
        else:
            self.head = runner.next
        if runner.next is not None:
            print('runner.next is not None')
            runner.next.previous = runner.previous
        del runner
        print(f'New DList: {self}')
        return self
        

    def value(self, pos):
        if pos >= self.len():
            print(f'Error: Position {pos} is outside the bounds of the Doubly Linked List.')
            return self
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
        temp_list = []
        runner = self.head
        i = 0
        while runner is not None:
            if runner.value in temp_list:
                self.remove_at(i)
            else:
                temp_list.append(runner.value)
                i += 1
            runner = runner.next


    def assign_next_node(self, node):
        pass


    def assign_previous_node(self, node):
        pass


    def is_circular_list(self):
        pass


    def reverse(self):
        pass
