class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Runtime: 16 ms
        # Memory: 13.6 MB
        return " ".join(s.split()[:k])
