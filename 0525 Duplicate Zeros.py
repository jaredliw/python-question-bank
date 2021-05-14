class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # Runtime: 1116 ms
        # Memory: 13.8 MB
        idx = 0
        while idx < len(arr):
            if arr[idx] == 0:
                for ptr in range(len(arr) - 1, idx, -1):
                    arr[ptr] = arr[ptr - 1]
                idx += 1
            idx += 1


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # Runtime: 52 ms
        # Memory: 13.6 MB
        idx = 0
        while idx < len(arr):
            if arr[idx] == 0:
                arr.pop()
                arr.insert(idx + 1, 0)
                idx += 1
            idx += 1