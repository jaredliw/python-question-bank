class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 108 ms
        # Memory: 15 MB
        _max = max(nums)
        # Formula for an arithmetic sequence
        ans = _max * (_max + 1) // 2 - sum(nums)
        return _max + 1 if ans == 0 and 0 in nums else ans
