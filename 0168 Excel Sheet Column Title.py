class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        # Runtime: 20 ms
        # Memory: 13.3 MB
        colname = ""
        while True:
            columnNumber, mod = divmod(columnNumber, 26)
            if mod == 0:
                colname += "Z"
                columnNumber -= 1
            else:
                colname += chr(mod + 64)
            if columnNumber == 0:
                break
        return colname[::-1]
