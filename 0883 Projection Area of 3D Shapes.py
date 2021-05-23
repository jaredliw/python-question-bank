class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Runtime: 60 ms
        # Memory: 13.5 MB
        row_max = [0] * len(grid)
        col_max = [0] * len(grid[0])
        non_zero_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                row_max[row] = max(row_max[row], grid[row][col])
                col_max[col] = max(col_max[col], grid[row][col])
                if grid[row][col] != 0:
                    non_zero_count += 1
        return non_zero_count + sum(row_max) + sum(col_max)