# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Runtime: 24 ms
        # Memory: 13.4 MB
        if head is None:
            return None
        
        ptr = head
        length = 0
        while ptr is not None:
            length += 1
            ptr = ptr.next
        k %= length
        if k == 0:
            return head
        
        ptr = head
        idx = 0
        while ptr.next is not None:
            if idx == length - k - 1:
                new_head = ptr.next
                ptr.next = None
                ptr = new_head
            else:
                ptr = ptr.next
            idx += 1
        ptr.next = head
        return new_head
