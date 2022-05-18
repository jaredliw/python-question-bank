class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Runtime: 108 ms
        # Memory: 14.6 MB
        def __search(find_last_occurrence = False):  # Default to find first occurrence
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left + right + 1) // 2 if find_last_occurrence else (left + right) // 2
                if nums[mid] == target:
                    if find_last_occurrence:
                        left = mid
                    else:
                        right = mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            if len(nums) == 0 or nums[left] != target:
                return -1
            return left

        first_occurrence = __search()
        if first_occurrence == -1:
            return [-1, -1]
        return first_occurrence, __search(True)
