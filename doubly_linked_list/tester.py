from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList


x = ListNode(12)
print(x.value, x.prev, x.next)

x.insert_after(99)
print(x.value, x.prev, x.next.value)

x.insert_before(30)
print(x.value, x.prev.value, x.next.value)

node = ListNode(10)
dll = DoublyLinkedList(node)
print(dll.head.value, dll.tail.value)

dll.add_to_head(5)
print(dll.head.value, dll.tail.value)

dll.add_to_tail(15)
print(dll.head.value, dll.tail.value)

dll.remove_from_head()
print(dll.head.value, dll.tail.value)

dll.remove_from_tail()
print(dll.head.value, dll.tail.value)

dll.add_to_head(5)
print(dll.head.value, dll.tail.value)

dll.add_to_tail(15)
print(dll.head.value, dll.tail.value)

node_1 = ListNode(3)
node_2 = ListNode(4)
node_3 = ListNode(5)

node_1.next = node_2
node_2.next = node_3
node_2.prev = node_1
node_3.prev = node_2

node_1.delete()
print(node_2.value)

# node_1.delete()
# print(node_2.prev.value, node_2.next.value)

dll.move_to_front(dll.head.next)
print(dll.head.value, dll.tail.value)

print(dll.get_max())
