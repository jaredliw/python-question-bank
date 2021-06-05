class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        # Runtime: 24 ms
        # Memory; 13.6 MB
        visited = {(0, 0),}
        x = 0
        y = 0
        for p in path:
            if p == "N":
                x += 1
            elif p == "S":
                x -= 1
            elif p == "E":
                y += 1
            else:
                y -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False
