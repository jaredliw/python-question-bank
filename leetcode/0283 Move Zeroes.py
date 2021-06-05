class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Runtime: 40 ms
        # Memory: 14.3 MB
        ptr = 0
        for num in nums:
            if num != 0:
                nums[ptr] = num
                ptr += 1
        while ptr < len(nums):
            nums[ptr] = 0
            ptr += 1
