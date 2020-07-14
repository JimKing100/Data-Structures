from binary_search_tree import BSTNode
import random


root = BSTNode(8)
root.insert(3)
print(root.left.value)
root.insert(10)
print(root.left.value, root.right.value)
root.in_order_print(root)
print(root.contains(3))
print(root.contains(5))
print(root.get_max())

arr = []
cb = lambda x: arr.append(x)

v1 = 15
v2 = 20
v3 = 25
v4 = 30
v5 = 35

root.insert(v1)
root.insert(v2)
root.insert(v3)
root.insert(v4)
root.insert(v5)

root.in_order_print(root)

root.for_each(cb)

for i in range(0, 6):
    print(arr[i])

root.bft_print(root)
