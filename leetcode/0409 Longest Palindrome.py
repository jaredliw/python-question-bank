class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 24 ms
        # Memory: 13.7 MB
        length = 0
        seen = set()  # You may use list too
        for char in s:
            if char in seen:
                seen.remove(char)
                length += 2
            else:
                seen.add(char)
        if seen:
            return length + 1
        else:
            return length
