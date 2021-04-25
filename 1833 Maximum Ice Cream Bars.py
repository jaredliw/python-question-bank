class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        # Runtime: 884 ms
        # Memory: 25.3 MB
        costs.sort()
        count = 0
        for cost in costs:
            if cost <= coins:
                coins -= cost
                count += 1
            else:
                break
        return count
