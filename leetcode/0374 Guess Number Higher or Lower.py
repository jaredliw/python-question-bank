# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Runtime: 8 ms
        # Memory: 13.2 MB

        # Binary search algorithm
        start = 0
        while True:
            mid = (start + n) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                n = mid - 1
            else:
                start = mid + 1
