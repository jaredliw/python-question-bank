class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # Runtime: 24 ms
        # Memory: 13.4 MB
        count = 0
        num = x ^ y
        while num > 0:
            count += num % 2
            num >>= 1
        return count


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # Runtime: 12 ms
        # Memory: 13.4 MB
        return bin(x ^ y).count("1")
