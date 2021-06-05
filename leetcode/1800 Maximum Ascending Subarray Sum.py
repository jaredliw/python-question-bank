class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 12 ms
        # Memory: 13.2 MB
        max_sum = 0
        cur_sum = 0
        last = 0
        for num in nums:
            if num > last:
                cur_sum += num
            else:
                max_sum = max(max_sum, cur_sum)
                cur_sum = num
            last = num
        return max(max_sum, cur_sum)
