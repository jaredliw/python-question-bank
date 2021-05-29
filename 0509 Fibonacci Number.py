class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Runtime: 12 ms
        # Memory: 13.6 MB
        if n <= 1:
            return n
        else:
            num1 = 0
            num2 = 1
            for _ in range(n - 1):
                num1, num2 = num2, num1 + num2
            return num2
