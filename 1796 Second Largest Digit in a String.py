from bisect import insort


class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 28 ms
        # Memory: 13.5 MB
        digits = []
        for char in s:
            if char.isdigit() and char not in digits:
                insort(digits, char)
        if len(digits) >= 2:
            return int(digits[-2])
        else:
            return -1
