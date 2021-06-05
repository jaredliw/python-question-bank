class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        # Runtime: 24 ms
        # Memory: 13.5 MB
        num = 0
        for idx, char in enumerate(columnTitle[::-1]):
            num += (ord(char) - 64) * 26 ** idx  # Base 26 -> Base 10
        return num
