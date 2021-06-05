class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # Runtime: 28 ms
        # Memory: 13.5 MB
        _max = max(candies)
        return map(lambda x: x + extraCandies >= _max, candies)
