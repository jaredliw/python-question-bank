class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 40 ms
        # Memory: 13.5 MB
        max_ = -1
        second_max = -1
        for num in nums:
            if num > max_:
                max_, second_max = num, max_
            elif num > second_max:
                second_max = num
        return (max_ - 1) * (second_max - 1)
