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
        self.listhead = None
        self.listtail = None


    def __str__(self):
        rep = '{'
        runner = self.head()
        while runner is not None:
            rep += f'\n\t{runner}'
            if runner.next is not None:
                rep += ', '
            runner = runner.next
        rep += '\n}'
        return rep


    def head(self):
        return self.listhead


    def tail(self):
        return self.listtail

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head()
        new_node.previous = None
        if self.head() is not None:
            self.head().previous = new_node
        self.listhead = new_node
        if self.listtail is None:
            self.listtail = new_node
        return self


    def append(self, value):
        new_node = Node(value)
        runner = self.tail()
        if runner is not None:
            new_node.previous = runner
            new_node.next = None
            runner.next = new_node
            self.listtail = new_node
        else:
            self.listhead = new_node
            self.listtail = new_node
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
            runner = self.head()
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
        runner = self.head()
        while i < pos and runner is not None:
            runner = runner.next
            i += 1
        if runner.previous is not None:
            runner.previous.next = runner.next
        else:
            self.listhead = runner.next
        if runner.next is not None:
            runner.next.previous = runner.previous
        else:
            self.listtail = runner.previous
        del runner
        return self
        

    def value(self, pos):
        if pos >= self.len():
            print(f'Error: Position {pos} is outside the bounds of the Doubly Linked List.')
            return self
        runner = self.head()
        counter = 0
        while counter != pos and runner is not None:
            counter += 1
            runner = runner.next
        return runner.value


    def len(self):
        counter = 0
        runner = self.head()
        while runner is not None:
            runner = runner.next
            counter += 1
        return counter


    def remove_duplicates(self):
        temp_list = []
        runner = self.head()
        i = 0
        while runner is not None:
            if runner.value in temp_list:
                self.remove_at(i)
            else:
                temp_list.append(runner.value)
                i += 1
            runner = runner.next
        return self


    def assign_next_node(self, node):
        pass


    def assign_previous_node(self, node):
        pass


    def is_circular_list(self):
        pass


    def reverse(self):
        print()
        runner = self.head()
        self.linktail = runner
        # Swap the links around and then go to previous, which used to be next
        while runner is not None:
            print(f'Node before: {runner}')
            runner.previous, runner.next = runner.next, runner.previous
            print(f'Node after: {runner}')
            if runner.previous is None:
                self.listhead = runner
            runner = runner.previous
        return self
