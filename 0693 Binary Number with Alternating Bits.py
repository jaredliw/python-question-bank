class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Runtime: 24 ms
        # Memory: 13.3 MB
        binary_n = bin(n)[2:]
        last = 0
        for d in binary_n:
            if d == last:
                return False
            last = d
        return True


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Runtime: 12 ms
        # Memory: 13.4 MB
        bit = n ^ (n >> 1)  # bit = 111... if n has alternating bits
        return bit & (bit + 1) == 0  # Check if all bits are 1


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Runtime: 20 ms
        # Memory: 13.4 MB
        bit = n ^ (n >> 2)  # bit = 1000... if n has alternating bits
        return bit & (bit - 1) == 0  # 1000... & 0111... = 0
