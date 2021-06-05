class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Runtime: 192 ms
        # Memory: 15.8 MB
        left = 0
        right = len(nums) - 1
        ans = [None] * len(nums)
        for idx in range(len(ans) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                ans[idx] = nums[left] ** 2
                left += 1
            else:
                ans[idx] = nums[right] ** 2
                right -= 1
        return ans


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for idx in range(len(nums)):
            nums[idx] **= 2
        nums.sort()
        return nums
