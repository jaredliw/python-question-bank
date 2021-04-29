class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Runtime: 16 ms
        # Memory: 13.5 MB
        try:
            while True:
                nums.remove(val)
        except ValueError:
            return len(nums)
