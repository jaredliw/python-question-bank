from math import sqrt

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Runtime: 16 ms
        # Memory: 13.5 MB

        # 1 + 2 + 3 + ... + (k-1) + k <= n, find maximum k.
        # Formula for the sum of an arithmetic sequence:
        # k * (k + 1) / 2 <= n
        # k^2 + k <= 2n
        # k^2 + k - 2n <= 0
        # Quadratic formula:
        # (-b (+ or -) sqrt(b^2 - 4ac)) / 2a
        # From above, a = 1, b = 1, c = -2n
        # (-1 (+ or -) sqrt(1^2 - 4(1)(-2n))) / 2(1)
        # = (-1 (+ or -) sqrt(8n + 1)) / 2

        # Formula:
        # k = floor((sqrt(8n + 1) - 1) / 2)
        return int((sqrt(n * 8 + 1) - 1) // 2)
