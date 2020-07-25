import math


class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        deleted = self.storage[0]
        self.storage[0] = self.storage[len(self.storage) - 1]
        self.storage.pop()
        self._sift_down(0)
        return deleted

    def get_max(self):
        return(self.storage[0])

    def get_size(self):
        return(len(self.storage))

    def _bubble_up(self, index):
        if index == 0:
            return
        child = self.storage[index]
        parent_index = int(math.floor(index-1)/2)
        parent = self.storage[parent_index]
        if parent < child:
            self.storage[parent_index] = child
            self.storage[index] = parent
            self._bubble_up(parent_index)

    def _sift_down(self, index):
        # No children
        if len(self.storage) < ((2 * index) + 2):
            return
        # Left child only
        elif len(self.storage) < ((2 * index) + 3):
            parent = self.storage[index]
            lchild = self.storage[(2 * index) + 1]
            if parent < lchild:
                self.storage[index] = lchild
                self.storage[(2 * index) + 1] = parent
                self._sift_down((2 * index) + 1)
        # Both children
        else:
            parent = self.storage[index]
            lchild = self.storage[(2 * index) + 1]
            rchild = self.storage[(2 * index) + 2]
            if parent < max(lchild, rchild):
                if lchild > rchild:
                    self.storage[index] = lchild
                    self.storage[(2 * index) + 1] = parent
                    self._sift_down((2 * index) + 1)
                else:
                    self.storage[index] = rchild
                    self.storage[(2 * index) + 2] = parent
                    self._sift_down((2 * index) + 2)
