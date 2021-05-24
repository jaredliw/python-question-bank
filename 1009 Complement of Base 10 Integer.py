class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Runtime: 12 ms
        # Memory: 13.4 MB
        ans = 1
        while ans < N:
            ans <<= 1
            ans += 1
        return ans ^ N


from math import log


class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Runtime: 8 ms
        # Memory: 13.2 MB
        return 1 if N == 0 else N ^ (2 ** int(log(N, 2) + 1) - 1)


class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Runtime: 20 ms
        # Memory: 13.4 MB
        return 1 if N == 0 else N ^ (2 ** N.bit_length() - 1)
