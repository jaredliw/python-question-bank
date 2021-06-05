class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 12 ms
        # Memory: 13.4 MB
        return len(s.split())
