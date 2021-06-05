class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        # Runtime: 44 ms
        # Memory: 13.7 MB
        new_arr = []
        ptr1 = 0
        for ptr2 in range(n, 2 * n):
            new_arr.append(nums[ptr1])
            new_arr.append(nums[ptr2])
            ptr1 += 1
        return new_arr


# Python 2 only
from itertools import cycle


class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        # Runtime: 44 ms
        # Memory: 13.6 MB
        return list(it.next() for it in cycle([iter(nums[:n]), iter(nums[n:])]))
