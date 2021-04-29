class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        # Runtime: 16 ms
        # Memory: 13.3 MB
        height = 0
        highest = 0
        for g in gain:
            height += g
            highest = max(height, highest)
        return highest
