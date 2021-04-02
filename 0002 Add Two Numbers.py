# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Runtime: 52 ms
        # Memory: 13.6 MB
        last_div = 0
        head = None
        for val1, val2 in self.iterLists(l1, l2):
            div, mod = divmod(val1 + val2 + last_div, 10)
            if head is None:
                head = ListNode(mod)
                cur = head
            else:
                cur.next = ListNode(mod)
                cur = cur.next
            last_div = div
        if last_div != 0:
            cur.next = ListNode(last_div)
        return head

    def iterLists(self, l1, l2):
        while True:
            cond1 = l1 is None
            cond2 = l2 is None
            if cond1 and cond2:
                break
            if cond1:
                val1 = 0
            else:
                val1 = l1.val
                l1 = l1.next
            if cond2:
                val2 = 0
            else:
                val2 = l2.val
                l2 = l2.next
            yield val1, val2
