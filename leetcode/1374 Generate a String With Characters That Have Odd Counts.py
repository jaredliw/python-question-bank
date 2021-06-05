class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Runtime: 16 ms
        # Memory: 13.5 MB
        if n % 2 == 0:
            return "a" * (n - 1) + "b"
        else:
            return "a" * n
