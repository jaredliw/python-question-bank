class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Runtime: 16 ms
        # Memory: 13.4 MB
        s = s.split()
        s.sort(key=lambda x: x[-1])
        return " ".join(map(lambda x: x[:-1], s))
