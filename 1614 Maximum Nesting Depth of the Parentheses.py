class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 24 ms
        # Memory: 13.4 MB
        cur_depth = 0
        max_depth = 0
        for char in s:
            if char in "([{":
                cur_depth += 1
            elif char in ")]}":
                cur_depth -= 1
            if cur_depth > max_depth:
                max_depth = cur_depth
        return max_depth
