class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Runtime: 8 ms
        # Memory: 13.4 MB
        n_match = 0
        while n != 1:
            if n % 2 == 0:
                n_match += n // 2
                n //= 2
            else:
                n_match += (n - 1) // 2
                n = (n - 1) / 2 + 1
        return n_match
