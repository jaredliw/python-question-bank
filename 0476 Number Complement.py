class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Runtime: 20 ms
        # Memory: 13.2 Mb
        ans = 1
        while ans < num:
            ans <<= 1
            ans += 1
        return ans ^ num


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Runtime: 16 ms
        # Memory: 13.5 MB

        # n ^ complement = 111... <-> n ^ 111... = complement
        return num ^ (2 ** int(log(num, 2) + 1) - 1)  # Find how many 1 is needed
