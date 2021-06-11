# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Runtime: 20 ms
        # Memory: 13.5 MB
        dummy = ListNode()
        new = dummy
        while l1 is not None or l2 is not None:
            if l1 is None:
                new.next = l2
                l2 = l2.next
            elif l2 is None:
                new.next = l1
                l1 = l1.next
            elif l1.val <= l2.val:
                new.next = l1
                l1 = l1.next
            else:
                new.next = l2
                l2 = l2.next
            new = new.next
        return dummy.next
