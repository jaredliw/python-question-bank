from itertools import izip_longest  # In Python 3, it is zip_longest


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # Runtime: 16 ms
        # Memory: 13.8 MB
        return "".join(map(lambda x: x[0] + x[1], izip_longest(word1, word2, fillvalue="")))
