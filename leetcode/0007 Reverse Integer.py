class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Runtime: 16 ms
        # Memory: 13.3 MB
        if x < 0:
            ans = int(str(x * -1)[::-1]) * -1
        else:
            ans = int(str(x)[::-1])
        if ((-2) ** 31) <= ans <= (2 ** 31 - 1):
            return ans
        else:
            return 0


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Runtime: 28 ms
        # Memory: 13.6 Mb

        # Pure math solution
        neg = x < 0
        x = abs(x)
        reversed_num = 0
        while x != 0:
            # Move the digits to the left by 1
            reversed_num *= 10
            # Add the least significant digit of x to it
            reversed_num += x % 10
            # Remove 1 digit from the right
            x /= 10
        if neg:
            reversed_num = -reversed_num
        if -2 ** 31 <= reversed_num <= 2 ** 31 - 1:
            return reversed_num
        else:
            return 0
