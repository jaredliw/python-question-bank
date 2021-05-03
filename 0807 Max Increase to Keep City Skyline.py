class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Runtime: 60 ms
        # Memory: 13.5 MB

        # Increase the heights of buildings as high as you can under the premise of max(column) and max(row) must remain
        # the same.
        # Thus, grid[i][j] = min(max[i][:], max[:][j]).
        size = len(grid)
        row_max = [0] * size
        col_max = [0] * size

        # Get skylines
        for row in range(size):
            for col in range(size):
                if grid[row][col] > row_max[row]:
                    row_max[row] = grid[row][col]
                if grid[row][col] > col_max[col]:
                    col_max[col] = grid[row][col]

        sum_increased = 0
        for row in range(size):
            for col in range(size):
                sum_increased += min(row_max[row], col_max[col]) - grid[row][col]
        return sum_increased
