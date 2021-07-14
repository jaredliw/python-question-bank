# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Runtime: 28 ms
        # Memory: 14.4 MB
        lthead = ListNode(-1)
        ltlist = lthead
        gehead = ListNode(-1)
        gelist = gehead
        
        cur_node = head
        while cur_node is not None:
            if cur_node.val < x:
                ltlist.next = cur_node
                ltlist = ltlist.next
            else:
                gelist.next = cur_node
                gelist = gelist.next
            cur_node = cur_node.next
        ltlist.next = gehead.next
        gelist.next = None
        return lthead.next