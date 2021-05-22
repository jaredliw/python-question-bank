class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        # Runtime: 128 ms
        # Memory: 13.8 MB
        boxTypes.sort(key=lambda x: x[1])
        size = 0
        idx = len(boxTypes) - 1
        while truckSize > 0:
            if idx < 0:
                break
            n = min(boxTypes[idx][0], truckSize)
            truckSize -= n
            size += boxTypes[idx][1] * n
            idx -= 1
        return size
