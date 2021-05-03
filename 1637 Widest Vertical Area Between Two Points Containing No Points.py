class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Runtime: 788 ms
        # Memory: 57.1 MB
        # y-coordinates are trivial here
        points.sort(key=lambda x: x[0])
        return max(map(lambda idx: points[idx][0] - points[idx - 1][0], range(1, len(points))))
