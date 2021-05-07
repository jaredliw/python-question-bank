class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Runtime: 16 ms
        # Memory: 13.2 MB
        return "{:,}".format(n).replace(",", ".")
