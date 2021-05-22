class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        # Runtime: 688 ms
        # Memory: 15.5 MB
        return min(len(set(candyType)), len(candyType) // 2)
