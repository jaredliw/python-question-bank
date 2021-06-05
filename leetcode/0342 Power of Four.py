from math import log


class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Runtime: 12 ms
        # Memory: 13.3 MB
        return log(n, 4).is_integer() if n > 0 else False
