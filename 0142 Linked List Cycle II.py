# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Runtime: 40 ms
        # Memory: 19.7 MB

        # Floyd's cycle-finding algorithm
        if head is None:
            return None

        fast_ptr = head
        slow_ptr = head
        while fast_ptr.next is not None and fast_ptr.next.next is not None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            if fast_ptr is slow_ptr:
                # reset one pointer to the head
                fast_ptr = head
                while fast_ptr is not slow_ptr:
                    fast_ptr = fast_ptr.next  # fast_ptr is no longer "fast" now
                    slow_ptr = slow_ptr.next
                # Two pointers will meet at the node where the cycle begins
                return fast_ptr  # "return slow_ptr" does the job as well
        return None
