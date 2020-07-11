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
