from itertools import izip_longest  # It's zip_longest in Python 3


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Runtime: 32 ms
        # Memory: 13.6 MB
        ans = ""
        last = 0
        for n1, n2 in izip_longest(num1[::-1], num2[::-1], fillvalue=0):
            last, mod = divmod(int(n1) + int(n2) + last, 10)
            ans += str(mod)
        if last != 0:
            ans += str(last)
        return ans[::-1]
