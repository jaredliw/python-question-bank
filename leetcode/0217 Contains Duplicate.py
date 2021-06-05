class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Runtime: 92 ms
        # Memory: 20 MB
        return len(nums) != len(set(nums))


from collections import Counter


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Runtime: 104 ms
        # Memory: 19.6 MB
        return Counter(nums).most_common(1)[0][1] != 1
