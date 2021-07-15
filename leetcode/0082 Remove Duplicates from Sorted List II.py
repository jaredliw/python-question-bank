# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Runtime: 44 ms
        # Memory: 14 MB
        dummy = ListNode(-1, head)
        last = dummy
        cur = head
        duplicated = False
        while cur is not None and cur.next is not None:
            if cur.val == cur.next.val:
                duplicated = True
            elif duplicated:
                last.next = cur.next
                duplicated = False
            else:
                last = last.next
            cur = cur.next
        if duplicated:
            last.next = None
        return dummy.next
