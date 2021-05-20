class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Runtime: 64 ms
        # Memory: 13.5 MB
        surface_area = 0
        # Left
        for row in range(len(grid)):
            last = 0
            for col in range(len(grid[0])):
                diff = grid[row][col] - last
                if diff > 0:
                    surface_area += diff
                last = grid[row][col]

        # Right
        for row in range(len(grid)):
            last = 0
            for col in range(len(grid[0]) - 1, -1, -1):
                diff = grid[row][col] - last
                if diff > 0:
                    surface_area += diff
                last = grid[row][col]

        # Back
        for col in range(len(grid[0])):
            last = 0
            for row in range(len(grid)):
                diff = grid[row][col] - last
                if diff > 0:
                    surface_area += diff
                last = grid[row][col]

        # Front
        for col in range(len(grid[0]) - 1, -1, -1):
            last = 0
            for row in range(len(grid)):
                diff = grid[row][col] - last
                if diff > 0:
                    surface_area += diff
                last = grid[row][col]

        # Up / Down
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] > 0:
                    surface_area += 2
        return surface_area
