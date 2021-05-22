class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        # Runtime: 28 ms
        # Memory: 14.1 MB
        if start > destination:
            start, destination = destination, start
        return min(sum(distance[start:destination]), sum(distance[:start] + distance[destination:]))
