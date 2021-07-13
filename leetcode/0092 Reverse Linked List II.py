# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # Runtime: 40 ms
        # Memory: 14.5 MB
        dummy_node = ListNode()
        dummy_node.next = head

        node_before = dummy_node
        for _ in range(left - 1):
            node_before = node_before.next
        left_node = node_before.next

        right_node = node_before
        for _ in range(right - left + 1):
            right_node = right_node.next
        node_after = right_node.next

        # Break the chain
        node_before.next = None
        right_node.next = None

        # Reverse
        last_node = None
        cur_node = left_node
        while cur_node is not None:
            temp_node = cur_node.next
            cur_node.next = last_node
            last_node = cur_node
            cur_node = temp_node

        # Chain them back
        node_before.next = right_node
        left_node.next = node_after
        return dummy_node.next
