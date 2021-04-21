class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Runtime: 40 ms
        # Memory: 14.2 MB
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            for idx in range(len(nums) - 1):
                if nums[idx] < target <= nums[idx + 1]:
                    return idx + 1


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Runtime: 32 ms
        # Memory: 14.1 MB
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
