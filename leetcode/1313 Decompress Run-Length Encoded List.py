class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Runtime: 52 ms
        # Memory: 13.8 MB
        new = []
        for idx in range(0, len(nums), 2):
            new.extend([nums[idx + 1]] * nums[idx])
        return new
