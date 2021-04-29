class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Runtime: 16 ms
        # Memory: 13.4 MB
        expected = sorted(heights)
        count = 0
        for item1, item2 in zip(heights, expected):
            if item1 != item2:
                count += 1
        return count
