from functools import reduce

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        # Runtime: 20 ms
        # Memory: 13.6 MB
        return reduce(lambda n, stone: n + 1 if stone in jewels else n, stones, 0)
