class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 26 ms
        # Memory: 13.5 MB
        left = 0
        right = len(nums)
        while left <= right:
            mid = (left + right) // 2
            gt_mid_count = reduce(lambda accum, x: accum + 1 if x >= mid else accum, nums, 0)
            if gt_mid_count == mid:
                return mid
            elif gt_mid_count < mid:
                right = mid - 1
            else:
                left = mid + 1
        return -1
