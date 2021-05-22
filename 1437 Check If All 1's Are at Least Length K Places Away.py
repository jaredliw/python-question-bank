class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Runtime: 460 ms
        # Memory: 17.7 MB
        try:
            last_1_idx = nums.index(1)
        except ValueError:
            return True
        for idx in range(last_1_idx + 1, len(nums)):
            if nums[idx]:
                if idx - last_1_idx < k + 1:
                    return False
                last_1_idx = idx
        return True
