class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # Runtime: 36 ms
        # Memory: 13.5 MB
        return max(map(sum, accounts))
