class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 76 ms
        # Memory: 15.3 MB
        idx = 0
        last_num = None
        while idx < len(nums):
            if nums[idx] == last_num:
                nums.pop(idx)
            else:
                last_num = nums[idx]
                idx += 1
        return len(nums)


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 52 ms
        # Memory: 15.2 MB
        nums[:] = sorted(set(nums))
        return len(nums)
