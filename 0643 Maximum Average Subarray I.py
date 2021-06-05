class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Runtime: 1396 ms
        # Memory: 23.1 MB
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for idx in range(len(nums) - k):
            window_sum += nums[idx + k] - nums[idx]
            if window_sum > max_sum:
                max_sum = window_sum
        return max_sum / float(k)
