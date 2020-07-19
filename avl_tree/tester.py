from avl_tree import Node
from avl_tree import AVLTree


tree = AVLTree()
print(tree.height)
tree.node = Node(5)
tree.update_height()
print(tree.height)

print(tree.node.key, tree.node.left, tree.node.right)
# tree.insert(3)
# print(tree.node.left.key)
# tree.insert(6)
# print(tree.node.right.key)
tree.node.left = AVLTree(Node(3))
tree.update_height()
tree.update_balance()
tree.display()
tree.node.right = AVLTree(Node(6))
tree.update_height()
tree.update_balance()
tree.display()
tree.node.right.node.right = AVLTree(Node(8))
tree.update_height()
tree.update_balance()
tree.display()
