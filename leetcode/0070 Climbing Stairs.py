class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Runtime: 20 ms
        # Memory: 13.3 MB

        # It is actually a fibonacci sequence, where Xn = Xn-1 + Xn-2
        # if we can climb 1, 2 or 3 steps at a time, then Xn = Xn-1 + Xn-2 + Xn-3 and so as for n steps
        fib1 = 1
        fib2 = 2
        if n == 1:
            return fib1
        elif n == 2:
            return fib2
        for _ in range(n - 2):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2


from math import sqrt


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Runtime: 16 ms
        # Memory: 13.4 MB

        # Find nth fibonacci number by formula
        # n + 1 because the sequence is start with "1, 2, ..." whereas the formula is for the sequence which starts
        # with "1, 1, ..."
        return int(((((1 + sqrt(5)) / 2) ** (n + 1)) - (((1 - sqrt(5)) / 2) ** (n + 1))) / sqrt(5))
