class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Shortcut solution
        # Runtime: 16 ms
        # Memory: 13.5 MB
        return bin(int(a, 2) + int(b, 2))[2:]  # remove leading "0b", str.lstrip() does not work with "0b0"


# Python 3 only
from itertools import zip_longest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Runtime: 36 ms
        # Memory: 14.2 MB
        ans = ""
        last = 0
        for char1, char2 in zip_longest(a[::-1], b[::-1], fillvalue=0):
            last, bit = divmod(int(char1) + int(char2) + last, 2)
            ans += str(bit)
        if last:
            ans += str(last)
        return ans[::-1]
