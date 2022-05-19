class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Runtime: 51 ms
        # Memory: 13.9 MB
        up = 0
        down = len(matrix) - 1
        while up < down:
            ctr = (up + down) // 2
            if matrix[ctr][-1] == target:
                return True
            elif matrix[ctr][-1] < target:
                up = ctr + 1
            else:
                down = ctr
        row = up

        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
