from itertools import groupby


class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Runtime: 12 ms
        # Memory: 13.4 MB
        max_len_1 = 0
        max_len_0 = 0
        for num, iterator in groupby(s):
            if num == "1":
                max_len_1 = max(max_len_1, len(list(iterator)))
            else:
                max_len_0 = max(max_len_0, len(list(iterator)))
        return max_len_1 > max_len_0


