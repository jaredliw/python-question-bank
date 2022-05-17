class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Runtime: 37 ms
        # Memory: 13.3 MB
        left = 0
        right = x
        while left < right:
            mid = (left + right + 1) // 2
            if mid ** 2 > x:
                right = mid - 1
            else:
                left = mid
        return left


# from math import sqrt
#
#
# class Solution(object):
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         # Runtime: 28 ms
#         # Memory: 14.2 MB
#         return int(sqrt(x))  # you may use isqrt for python >= 3.8
