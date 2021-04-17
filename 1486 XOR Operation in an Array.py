class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        # Runtime: 16 ms
        # Memory: 13.4 MB
        return reduce(lambda x, y: x ^ y, range(start, start + 2 * (n - 1) + 1, 2), 0)
