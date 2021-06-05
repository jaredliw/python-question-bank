# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Runtime: 28 ms
    # Memory: 13.6 MB
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = None
        while node.next is not None:
            node.val = node.next.val
            prev = node
            node = node.next
        prev.next = None
