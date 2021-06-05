class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        # Runtime: 16 ms
        # Memory: 13.5 MB
        new = []
        for idx, num in zip(index, nums):
            new.insert(idx, num)
        return new
