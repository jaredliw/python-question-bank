class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        # Runtime: 24 ms
        # Memory: 13.4 MB
        return "".join(word1) == "".join(word2)
