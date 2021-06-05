# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Runtime: 16 ms
        # Memory: 13.3 MB
        left = 1
        last = -1
        while left <= n:
            mid = (left + n) // 2
            if isBadVersion(mid):
                last = mid
                n = mid - 1
            else:
                left = mid + 1
        return last
