class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        # Runtime: 40 ms
        # Memory: 14.2 MB

        # Think about if the input was only one digit. Then you need to add up as many ones as the value of this digit.
        # If the input has multiple digits, then you can solve for each digit independently, and merge the answers to
        # form numbers that add up to that input.
        # Thus the answer is equal to the max digit.
        return int(max(str(n)))
