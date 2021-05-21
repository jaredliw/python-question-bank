class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Runtime: 44 ms
        # Memory: 13.5 MB
        steps = 0
        for idx in range(len(points) - 1):
            steps += max(abs(points[idx][0] - points[idx + 1][0]), abs(points[idx][1] - points[idx + 1][1]))
        return steps
