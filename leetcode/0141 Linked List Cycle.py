# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Runtime: 40 ms
        # Memory: 20.3 MB

        # Floyd's cycle-finding algorithm
        if head is None:
            return False

        fast_ptr = head
        slow_ptr = head
        while fast_ptr.next is not None and fast_ptr.next.next is not None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            if fast_ptr is slow_ptr:
                return True
        return False
