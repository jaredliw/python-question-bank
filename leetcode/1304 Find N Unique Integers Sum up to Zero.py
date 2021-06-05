class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Runtime: 12 ms
        # Memory: 13.5 MB
        ans = []
        if n % 2 == 1:
            ans.append(0)
        for num in range(1, n // 2 + 1):
            ans.append(num)
            ans.append(-num)
        return ans
