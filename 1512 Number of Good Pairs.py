from functools import reduce  # Remove this line in Python 2


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Python 2
        # Runtime: 24 ms
        # Memory: 13.5 MB

        # Python 3
        # Runtime: 24 ms
        # Memory: 14.3 MB
        distinct = set(nums)
        # Count how many times each number appears.
        # If a number appears n times, then n * (n – 1) // 2 good pairs can be made with this number.
        return reduce(lambda total, num: total + nums.count(num) * (nums.count(num) - 1) // 2, distinct, 0)
