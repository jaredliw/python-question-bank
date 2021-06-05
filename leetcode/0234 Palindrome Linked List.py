# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Runtime: 1036 ms
        # Memory: 67.6 MB
        half1_ptr = head
        half2_ptr = head
        while half1_ptr.next is not None and half1_ptr.next.next is not None:
            half1_ptr = half1_ptr.next.next
            half2_ptr = half2_ptr.next
        half1_ptr = head
        half2_ptr = half2_ptr.next
        # half2_ptr is now pointing to the middle of the linked list

        # Reverse the second half
        last_node = None
        while half2_ptr is not None:
            next_node = half2_ptr.next
            half2_ptr.next = last_node
            last_node = half2_ptr
            half2_ptr = next_node
        half2_ptr = last_node

        # Compare two halves
        while half1_ptr is not None and half2_ptr is not None:
            if half1_ptr.val != half2_ptr.val:
                return False
            half1_ptr = half1_ptr.next
            half2_ptr = half2_ptr.next
        return True
