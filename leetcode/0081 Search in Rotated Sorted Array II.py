class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def __find_pivot():
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[-1]:
                    left = mid + 1
                else:
                    right = mid
            return left

        for _ in range(len(nums)):
            if nums[0] == nums[-1]:
                nums.append(nums.pop(0))  # Rotate
            else:
                break
        pivot = __find_pivot()
        if pivot == 0:
            left = 0
            right = len(nums) - 1
        elif target > nums[-1]:
            left = 0
            right = pivot - 1
        else:
            left = pivot
            right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if nums[mid] != target:
            return False
        return True
