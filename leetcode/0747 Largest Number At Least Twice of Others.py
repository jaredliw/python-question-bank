class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = -1
        max_num_idx = -1
        for idx, num in enumerate(nums):
            if num > max_num:
                max_num = num
                max_num_idx = idx
        for num in nums:
            if num != max_num and num * 2 > max_num:
                return -1
        return max_num_idx
