class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Runtime: 20 ms
        # Memory: 13.5 MB
        if num < 0:
            num += 4294967296  # Two's complement, 4294967296 = 2 ** 32
        return hex(num)[2:]


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Runtime: 16 ms
        # Memory: 13.5 Mb
        if num == 0:
            return "0"
        elif num < 0:
            num += 4294967296  # Two's complement, 4294967296 = 2 ** 32
        ans = ""
        while num > 0:
            num, mod = divmod(num, 16)
            if mod >= 10:
                ans += chr(mod + 87)
            else:
                ans += str(mod)
        return ans[::-1]
