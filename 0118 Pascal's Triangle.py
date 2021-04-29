class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Runtime: 12 ms
        # Memory: 13.5 MB
        pascal = []
        for r in range(1, numRows + 1):
            row = []
            for c in range(r):
                if c == 0 or c == r - 1:
                    row.append(1)
                else:
                    last_row = pascal[-1]
                    row.append(last_row[c - 1] + last_row[c])
            pascal.append(row)
        return pascal
