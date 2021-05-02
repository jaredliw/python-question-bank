class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Runtime: 720 ms
        # Memory: 13.9 MB
        counts = []
        for center_x, center_y, radius in queries:
            count = 0
            # Euclidean distance formula:
            # sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            # If the distance between the center and the point is <= radius, the point is inside the circle
            # sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) <= radius
            # = (x2 - x1) ** 2 + (y2 - y1) ** 2 <= radius
            for x, y in points:
                if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
                    count += 1
            counts.append(count)
        return counts
