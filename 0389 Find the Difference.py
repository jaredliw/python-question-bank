class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Runtime: 28 ms
        # Memory: 13.6 MB
        for char in s:
            t = t.replace(char, "", 1)
        return t


# Remove the following line in python 2:
from functools import reduce


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Python 2:
        # Runtime: 24 ms
        # Memory: 13.4 MB

        # Python 3:
        # Runtime: 32 ms
        # Memory: 14.1 MB

        # Same concept as #136
        return chr(reduce(lambda accum, item: accum ^ ord(item), s + t, 0))


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Runtime: 16 ms
        # Memory: 13.6 MB

        # Same concept as #136
        return chr(sum(map(ord, t)) - sum(map(ord, s)))
