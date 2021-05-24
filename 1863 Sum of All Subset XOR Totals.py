from itertools import chain, combinations


class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 52 ms
        # Memory: 13.5 MB
        ans = 0
        for powerset in chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1)):
            xor_total = 0
            for item in powerset:
                xor_total ^= item
            ans += xor_total
        return ans
