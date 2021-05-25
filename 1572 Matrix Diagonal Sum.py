class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        # Runtime: 80 ms
        # Memory: 13.5 MB
        col = 0
        diag_sum = 0
        size = len(mat)
        for row in range(size):
            diag_sum += mat[row][col]
            if size - col - 1 != col:
                diag_sum += mat[row][size - col - 1]
            
            if size % 2 == 0 and row == size // 2 - 1:
                pass
            elif row < size // 2:
                col += 1
            else:
                col -= 1
        return diag_sum
