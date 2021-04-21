class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 36 ms
        # Memory: 14.4 MB
        distinct = list(set(nums))
        if len(distinct) < 3:
            return max(distinct)
        else:
            distinct.sort()
            return distinct[-3]
