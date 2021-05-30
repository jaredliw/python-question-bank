# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Runtime: 20 ms
        # Memory: 13.3 MB
        fast_ptr = head
        slow_ptr = None
        idx = 0
        while fast_ptr is not None:
            if slow_ptr is None:
                if idx == n:
                    slow_ptr = head
            else:
                slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
            idx += 1
        
        if slow_ptr is None:
            return head.next
        elif slow_ptr.next.next is None:
            slow_ptr.next = None
        else:
            slow_ptr.next = slow_ptr.next.next
        return head
