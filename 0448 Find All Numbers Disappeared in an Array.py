class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Runtime: 340 ms
        # Memory: 21 MB
        for idx in range(len(nums)):
            # Negative value means there is a number that can be placed at the index (means the number is idx + 1)
            if nums[abs(nums[idx]) - 1] > 0:
                nums[abs(nums[idx]) - 1] *= -1
        ans = []
        for idx, num in enumerate(nums):
            if num > 0:
                ans.append(idx + 1)
        return ans
