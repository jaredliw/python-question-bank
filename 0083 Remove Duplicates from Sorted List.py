# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Runtime: 32 ms
        # Memory: 13.4 MB
        if head is None:
            return None
        
        cur = head
        while cur.next is not None:
            if cur.next.val == cur.val:
                # Find next node
                ptr = cur.next.next
                while ptr is not None:
                    if ptr.val != cur.val:
                        break
                    ptr = ptr.next
                cur.next = ptr
            cur = cur.next
            if cur is None:
                break
        return head
