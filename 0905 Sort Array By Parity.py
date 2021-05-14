class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Runtime: 68 ms
        # Memory: 14.4 MB
        ptr1 = 0
        for ptr2 in range(len(nums)):
            if nums[ptr2] % 2 == 0:
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
                ptr1 += 1
        return nums
