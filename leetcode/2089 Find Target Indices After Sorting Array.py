class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Runtime: 52 ms
        # Memory: 13.3 MB
        nums.sort()

        # Finding the smallest index where nums[index] = target
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # Not found, return []
        if nums[left] != target:
            return []

        # Add the rest of the indices where nums[index] == target
        res = [left]
        for i in range(left + 1, len(nums)):
            if nums[i] == target:
                res.append(i)
            else:
                break
        return res
