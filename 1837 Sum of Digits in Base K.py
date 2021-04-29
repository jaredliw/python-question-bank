class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # Runtime: 16 ms
        # Memory: 13.4 MB
        d_sum = 0
        while n != 0:
            n, mod = divmod(n, k)
            d_sum += mod
        return d_sum
