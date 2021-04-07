class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        # Runtime: 20 ms
        # Memory: 13.6 MB

        # If column + row is even, black, else white
        return int(ord(coordinates[0]) - 96 + int(coordinates[1])) % 2
