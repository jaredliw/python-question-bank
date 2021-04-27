from functools import reduce  # Remove this line in Python 2


class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        # Runtime: 32 ms
        # Memory: 13.5 MB
        return reduce(lambda depth, log: max(depth - 1, 0) if log == "../" else depth + 1 if log != "./" else depth,
                      logs, 0)
