class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 48 ms
        # Memory: 14.4 mb

        # Kadane's algorithm
        global_max = nums[0]
        last_max = nums[0]
        for num in nums[1:]:
            last_max = max(last_max + num, num)
            global_max = max(global_max, last_max)
        return global_max
