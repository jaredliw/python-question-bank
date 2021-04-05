class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Runtime: 168 ms
        # Memory: 21.2 MB
        ptr1 = 0
        ptr2 = len(s) - 1
        while ptr1 < ptr2:
            s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
            ptr1 += 1
            ptr2 -= 1


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Runtime: 164 ms
        # Memory: 21 MB

        # Shortcut solution
        # The variable s and the original list are pointing to the same object, that means, when you modify the list
        # inside a function, the original list will get changed as well.
        # In here, if you do "s = s[::-1]", python will create a new object and s will point to the new one, leaving the
        # original list unchanged.
        # So, here is the trick of "s[:] = ..." which allows you to modify the original list.
        s[:] = s[::-1]
