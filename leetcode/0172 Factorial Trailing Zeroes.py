class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Runtime: 16 ms
        # Memory: 13.4 MB
        n_zeros = 0
        while True:
            n_divisible_by_5 = n // 5
            if n_divisible_by_5 == 0:
                break
            else:
                n_zeros += n_divisible_by_5
                n = n_divisible_by_5
        return n_zeros
