from functools import reduce  # Remove this line in Python 2


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 36 ms
        # Memory: 13.3 MB
        return reduce(lambda count, item: count + 1 if len(str(item)) % 2 == 0 else count, nums, 0)
