class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Runtime: 448 ms
        # Memory: 13.8 MB
        perimeter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    count = 4
                    if row != 0 and grid[row - 1][col]:
                        count -= 1
                    if row != len(grid) - 1 and grid[row + 1][col]:
                        count -= 1
                    if col != 0 and grid[row][col - 1]:
                        count -= 1
                    if col != len(grid[0]) - 1 and grid[row][col + 1]:
                        count -= 1
                    perimeter += count
        return perimeter
