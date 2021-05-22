class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Runtime: 56 ms
        # Memory: 15 MB
        
        # O(n) solution
        for idx in range(len(arr) - 1):
            if arr[idx + 1] < arr[idx]:
                return idx


class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Runtime: 52 ms
        # Memory: 14.7 MB
        
        # O(log n) solution
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            left_smaller = arr[mid - 1] < arr[mid]
            right_smaller = arr[mid + 1] < arr[mid]
            if left_smaller and right_smaller:
                return mid
            elif left_smaller:
                left = mid + 1
            else:
                right = mid - 1
