from math import sqrt  # you may use isqrt in python 3


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Runtime: 24 ms
        # Memory: 13.6 MB
        if num == 1:
            return False
        
        sum_factor = 0
        for factor in range(1, int(sqrt(num)) + 1):
            if num % factor == 0:
                sum_factor += factor
                sum_factor += num // factor
        return num == sum_factor - num
