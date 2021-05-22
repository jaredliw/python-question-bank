class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 60 ms
        # Memory: 14.5 MB
        ans = 0
        start = 0
        nums.append(-1)  # Dummy number
        for idx in range(1, len(nums)):
            if nums[idx] <= nums[idx - 1]:
                ans = max(ans, idx - start)
                start = idx
        return ans
