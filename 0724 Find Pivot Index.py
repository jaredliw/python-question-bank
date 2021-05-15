class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 124 ms
        # Memory: 14.5 MB
        left_sum = 0
        right_sum = sum(nums)
        last = 0
        for idx, num in enumerate(nums):
            left_sum += last
            right_sum -= num
            last = num
            if left_sum == right_sum:
                return idx
        return -1
