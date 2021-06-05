class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # Runtime: 16 ms
        # Memory: 13.9 MB
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
