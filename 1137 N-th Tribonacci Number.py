class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Runtime: 28 ms
        # Memory: 13.4 MB
        if n == 0:
            return 0
        elif n <= 2:
            return 1

        t0 = 0
        t1 = 1
        t2 = 1
        for _ in range(3, n + 1):
            t0, t1, t2 = t1, t2, t0 + t1 + t2
        return t2
