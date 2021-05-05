class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # runtime: 100 ms
        # Memory: 13.7 MB
        op = 0
        for idx, num in enumerate(nums):
            if idx > 0 and num <= nums[idx - 1]:
                to_incr = nums[idx - 1] - num + 1
                op += to_incr
                nums[idx] += to_incr
        return op
