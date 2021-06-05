class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for idx in range(1, len(nums)):
            nums[idx] += nums[idx - 1]
        return nums
