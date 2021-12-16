class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 115 ms
        # Memory: 15.5 MB
        left = 0
        right = 0
        window_sum = nums[0]
        min_window_size = float("inf")
        while True:
            try:
                if window_sum < target:
                    right += 1
                    window_sum += nums[right]
                else:
                    min_window_size = min(min_window_size, right - left + 1)
                    window_sum -= nums[left]
                    left += 1
            except IndexError:
                break
        return 0 if min_window_size == float("inf") else min_window_size
