from ctypes import create_string_buffer as string  # Mutable string


class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Runtime: 24 ms
        # Memory: 14.2 MB
        s = string(s)
        ptr1 = 0
        ptr2 = len(s) - 1
        while ptr1 < ptr2:
            if not s[ptr1].isalpha():
                ptr1 += 1
            elif not s[ptr2].isalpha():
                ptr2 -= 1
            else:
                s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
                ptr1 += 1
                ptr2 -= 1
        return s.value
