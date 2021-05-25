from math import sqrt


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # Runtime: 16 ms
        # Memory: 13.4 MB
        for num in range(int(sqrt(area)), 0, -1):
            if area % num == 0:
                return [area // num, num]
