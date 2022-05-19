class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 45 ms
        # Memory: 13.8 MB
        for _ in range(len(nums)):
            if nums[0] == nums[-1]:
                nums.append(nums.pop(0))  # Rotate
            else:
                break

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
