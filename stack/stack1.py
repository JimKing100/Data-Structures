"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""

from singly_linked_list import Node


class Stack:
    def __init__(self):
        self.size = 0
        self.head = None

    def __len__(self):
        return self.size

    def push(self, value):
        if self.head is None:
            # Handle the empty case
            self.head = Node(value)
        else:
            # Create a new node and it to the stack
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        self.size = self.size + 1

    def pop(self):
        if self.head is None:
            # Handle the empty case
            return None
        else:
            # Remove the head node from stack and make prior node new head
            pop_node = self.head
            self.head = self.head.next
            pop_node.next = None
            self.size = self.size - 1

            return pop_node.value
