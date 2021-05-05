class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 20 ms
        # Memory: 13.4 MB
        counts = {}
        for num in nums:
            counts.setdefault(num, 0)
            counts[num] += 1

        sum_unique = 0
        for num, count in counts.items():
            if count == 1:
                sum_unique += num
        return sum_unique
