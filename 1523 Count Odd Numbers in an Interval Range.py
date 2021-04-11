class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # Runtime: 12 ms
        # Memory: 13.4 MB

        # If low is even and high is even, no. of even = no. of odd + 1
        # If low is odd and high is odd, no. of even = no. of odd - 1
        # If low is odd and high is even, no. of even = no. of odd
        # If low is even and high is odd, no. of even = no. of odd
        return (high - low + 1) // 2 + 1 if low % 2 == high % 2 == 1 else (high - low + 1) // 2
