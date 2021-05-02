class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Runtime: 48 ms
        # Memory: 13.6 MB

        # After sorting the numbers, the index of each number is the number of items that are smaller than it
        # list.index returns the first index of value, so repeated numbers won't cause a problem
        sorted_nums = sorted(nums)
        counts = []
        for num in nums:
            counts.append(sorted_nums.index(num))
        return counts


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Runtime: 460 ms
        # Memory: 13.5 MB

        # Brute force solution
        counts = []
        for idx, num in enumerate(nums):
            count = 0
            for idx1, to_test in enumerate(nums):
                if idx == idx1:
                    continue
                elif to_test < num:
                    count += 1
            counts.append(count)
        return counts
