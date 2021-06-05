# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # Runtime: 24 ms
    # Memory: 15.3 MB

    # Iterative
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_nd = None
        while head is not None:
            next_nd = head.next
            head.next = prev_nd
            prev_nd = head
            head = next_nd
        return prev_nd


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # Runtime: 24 ms
    # Memory: 19.8 MB

    # Recursive
    def reverseList(self, head, prev_nd=None):
        """
        :type head: ListNode
        :type prev_nd: ListNode
        :rtype: ListNode
        """
        if head is None:
            return prev_nd

        next_nd = head.next
        head.next = prev_nd
        return self.reverseList(next_nd, head)
