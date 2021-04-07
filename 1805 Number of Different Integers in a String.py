import re

class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Runtime: 20 ms
        # Memory: 13.6 MB
        return len(set(map(int, re.findall("[0-9]+", word))))
