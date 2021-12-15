class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Runtime: 256 ms
        # Memory: 16 MB
        prefix_count = {0: 1}
        sum_ = 0
        ans = 0
        for num in nums:
            sum_ += num

            try:
                ans += prefix_count[sum_ - k]
            except KeyError:
                pass
            
            prefix_count.setdefault(sum_, 0)
            prefix_count[sum_] += 1
        return ans
