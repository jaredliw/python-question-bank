# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Runtime: 36 ms
        # Memory: 16.4 MB
        if head is None or head.next is None:
            return head
        odd_ptr = head
        even_ptr = head.next
        even_list = even_ptr
        while odd_ptr.next is not None and even_ptr.next is not None:
            odd_ptr.next = even_ptr.next
            odd_ptr = odd_ptr.next
            even_ptr.next = odd_ptr.next
            even_ptr = even_ptr.next
        odd_ptr.next = even_list
        return head
