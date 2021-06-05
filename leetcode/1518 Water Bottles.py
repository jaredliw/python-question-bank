class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        # Runtime: 16 ms
        # Memory: 13.4 MB
        drank = numBottles
        while numBottles >= numExchange:
            numBottles, mod = divmod(numBottles, numExchange)
            drank += numBottles
            numBottles += mod
        return drank
