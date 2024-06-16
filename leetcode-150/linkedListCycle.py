# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head) -> bool:
    visited_nodes=set()
    current_node = head
    while current_node:
        if current_node not in visited_nodes:
            visited_nodes.add(current_node)
        else:
            return True
        current_node = current_node.next
    return False

l1 = ListNode(2)
l2 = ListNode(0)
l3 = ListNode(-4)
l4 = ListNode(3)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l2

print(hasCycle(l1))

