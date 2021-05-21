import math


def angle(p1, p2):
    if p1 == p2:
        return 0

    k = (p2[1] - p1[1]) / math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    if k >= 0:
        if p2[0] >= p1[0]:  # First Quadrant
            return 2.0 * math.pi - math.asin(k)
        else:  # Second Quadrant
            return math.pi + math.asin(k)
    else:
        if p2[0] >= p1[0]:  # Fourth Quadrant
            return math.asin(-k)
        else:  # Third Quadrant
            return math.pi - math.asin(-k)


class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        # Runtime: 56 ms
        # Memory: 14 MB
        if len(coordinates) == 2:
            return True

        # Shoelace formula
        # 1. Order coordinates in CW direction
        # 1.1 Get a reference point (inside the polygon)
        ref_point = [0, 0]
        for point in coordinates:
            ref_point[0] += point[0]
            ref_point[1] += point[1]
        ref_point = [float(ref_point[0]) / len(coordinates), float(ref_point[1]) / len(coordinates)]

        # 1.2 Sort coordinates by angle
        coordinates.sort(key=lambda p: -angle(p, ref_point))

        # 2. Apply the formula
        shoelace1 = 0
        shoelace2 = 0
        coordinates.append(coordinates[0])
        for idx in range(len(coordinates)):
            if idx != len(coordinates) - 1:
                shoelace1 += coordinates[idx][0] * coordinates[idx + 1][1]
            if idx != 0:
                shoelace2 += coordinates[idx][0] * coordinates[idx - 1][1]
        return 0.5 * (shoelace1 - shoelace2) == 0


class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        # Runtime: 40 ms
        # Memory: 13.9 MB
        if len(coordinates) == 2:
            return True

        gradient = None
        for idx in range(1, len(coordinates)):
            try:
                cur_gradient = (coordinates[idx - 1][1] - coordinates[idx][1]) / (
                            coordinates[idx - 1][0] - coordinates[idx][0])
            except ZeroDivisionError:
                cur_gradient = float("inf")
            if gradient is None:
                gradient = cur_gradient
            elif cur_gradient != gradient:
                return False
        return True
