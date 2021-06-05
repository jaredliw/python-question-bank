class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Runtime: 12 ms
        # Memory: 13.3 MB
        return s.count("A") < 2 and "LLL" not in s
