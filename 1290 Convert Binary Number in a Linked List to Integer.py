# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        # Runtime: 24 ms
        # Memory: 13.5 MB
        head_cp = head
        bit_count = 0
        while head is not None:
            bit_count += 1
            head = head.next

        place_val = 1 << bit_count - 1  # Ewuivalent to place_val = 2 ** bit_count, but faster
        num = 0
        while head_cp is not None:
            if head_cp.val:
                num += place_val
            place_val >>= 1  # Equivalent to place_val //= 2, but faster
            head_cp = head_cp.next
        return num


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        # Runtime: 24 ms
        # Memory: 13.5 MB
        bin_str = ""
        while head is not None:
            bin_str += str(head.val)
            head = head.next
        return int(bin_str, 2)