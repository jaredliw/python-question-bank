# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        # Runtime: 180 ms
        # Memory: 43.2 MB

        # Count the length of llA
        ptr1 = headA
        count1 = 0
        while ptr1 is not None:
            count1 += 1
            ptr1 = ptr1.next

        # Count the length of llB
        ptr2 = headB
        count2 = 0
        while ptr2 is not None:
            count2 += 1
            ptr2 = ptr2.next

        # Calculate the absolute difference of legnths
        diff = abs(count1 - count2)

        # Ensure llA is always shorter than llB
        if count1 > count2:
            headA, headB = headB, headA

        # Move the longer one by diff steps
        while diff != 0:
            headB = headB.next
            diff -= 1

        # Move two pointers together until they are pointing to the same node
        while headA is not headB:
            headA = headA.next
            headB = headB.next

        return headA  # return headB
