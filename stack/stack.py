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


class Stack:
    def __init__(self):
        self.size = 0
        self.items = []

    def __len__(self):
        return self.size

    def push(self, value):
        # Add a value to the stack using a list
        self.items.append(value)
        self.size += 1

    def pop(self):
        # Remove a value from the stack using a list
        if self.items != []:
            self.size -= 1
            return self.items.pop()
