class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 258 ms
        # Memory: 13.4 MB
        max_count = 0
        count = 0
        cur = None
        for char in s:
            if char != cur:
                max_count = max(max_count, count)
                count = 0
                cur = char
            count += 1
        return max(max_count, count)
