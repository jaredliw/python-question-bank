class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Runtime: 36 ms
        # Memory: 13.6 MB
        hash_map = []
        for idx, num in enumerate(nums):
            pair = target - num
            if pair in hash_map:
                return [idx, hash_map.index(pair)]
            else:
                hash_map.append(num)
