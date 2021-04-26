# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # Runtime: 56 ms
        # Memory: 20.2 MB
        if head is None:
            return None

        if head.val == val:
            head = self.get_next(head.next, val)

        cur = head
        while cur is not None and cur.next is not None:
            if cur.next.val == val:
                cur.next = self.get_next(cur.next.next, val)
            cur = cur.next
        return head

    def get_next(self, ptr, val):
        while ptr is not None:
            if ptr.val != val:
                break
            ptr = ptr.next
        return ptr
