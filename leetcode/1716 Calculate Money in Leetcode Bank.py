class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Runtime: 16 ms
        # Memory: 13.3 MB
        n_week, n_day = divmod(n, 7)
        # Consider the arithmetic sequence: 28, 35, 42, ..., where the nth number is the sum of money in nth week
        # For the remain day, we have another arithmetic sequence: z, z + 1, z + 2, ..., where z = (no. of week + 1)
        # Formula for sum of first nth numbers in arithmetic sequence:
        # S_n = n / 2 * (2 * a + (n - 1) * d)
        return int(n_week * (56 + (n_week - 1) * 7) / 2 + n_day * (2 * (n_week + 1) + (n_day - 1)) / 2)
