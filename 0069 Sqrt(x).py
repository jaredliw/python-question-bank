from math import sqrt


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Runtime: 28 ms
        # Memory: 14.2 MB
        return int(sqrt(x))  # you may use isqrt for python >= 3.8
