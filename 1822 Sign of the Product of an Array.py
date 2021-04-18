from functools import reduce  # Remove this line in Python 2


class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 48 ms
        # Memory: 13.7 MB
        if 0 in nums:
            return 0
        elif reduce(lambda x, y: x + 1 if y < 0 else x, nums, 0) % 2:
            return -1
        else:
            return 1
