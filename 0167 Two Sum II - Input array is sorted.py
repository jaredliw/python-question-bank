class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Runtime: 52 ms
        # Memory: 13.4 MB
        ptr1 = 0
        ptr2 = len(numbers) - 1
        while ptr1 < ptr2:
            _sum = numbers[ptr1] + numbers[ptr2]
            if _sum == target:
                return [ptr1 + 1, ptr2 + 1]
            elif _sum < target:
                ptr1 += 1
            else:
                ptr2 -= 1
