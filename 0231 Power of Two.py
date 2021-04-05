class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Runtime: 20 ms
        # Memory: 13.4 MB

        # Numbers that is a power of 2: 0b1, 0b10, 0b100, 0b1000, ...
        # Have you noticed the pattern?
        return False if n <= 0 else bin(n).count("1") == 1


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Runtime: 20 ms
        # Memory: 13.5 MB
        # If n = 0b1000..., n - 1 = 0b01111.... then [n AND (n - 1)] = 0
        return n > 0 and not n & (n - 1)


# Python 3 only, python 2 has no log2 and log in python 2 is not precise
from math import log2

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Runtime: 24 ms
        # Memory: 14.1 MB
        return False if n <= 0 else log2(n).is_integer()
