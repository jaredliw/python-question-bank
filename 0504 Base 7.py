class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Runtime: 12 ms
        # Memory: 13.3 MB

        # Recursive
        if num < 0:
            return "-" + self.convertToBase7(abs(num))
        elif num < 7:
            return str(num)
        else:
            return self.convertToBase7(num // 7) + str(num % 7)


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Runtime: 16 ms
        # Memory: 13.2 MB
        base7 = ""
        neg = num < 0
        while num != 0:
            num, mod = divmod(abs(num), 7)
            base7 = str(mod) + base7
        if neg:
            return "-" + base7
        else:
            return base7