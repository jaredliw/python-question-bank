class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 20 ms
        # Memory: 13.5 MB
        stack = 0
        n_balanced = 0
        for char in s:
            if char == "L":
                stack += 1
            else:
                stack -= 1
            if stack == 0:
                n_balanced += 1
                stack = 0
        return n_balanced
