class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        # Runtime: 176 ms
        # Memory: 13.7 MB

        # Max R = 10 ** 6 = 20 bits, the longest binary will only have 20 digits
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        return reduce(lambda count, num: count + 1 if bin(num).count("1") in primes else count, range(L, R + 1), 0)
