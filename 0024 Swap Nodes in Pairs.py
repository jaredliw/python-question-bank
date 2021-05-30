# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Runtime: 16 ms
        # Memory: 13.5 MB
        cur = head
        last = None
        while cur is not None:
            if cur.next is not None:
                temp = cur.next.next
                cur.next.next = cur
                if last is not None:
                    last.next = cur.next
                if cur is head:
                    head = cur.next
                cur.next = temp
            last = cur
            cur = cur.next
        return head
