class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 44 ms
        # Memory: 13.4 MB
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        val = 0
        for idx, l in enumerate(s):
            # If a smaller roman is coming before a larger one, we subtract s[idx] from s[idx + 1].
            if idx != len(s) - 1 and mapping[l] < mapping[s[idx + 1]]:
                val += -mapping[l]
            else:
                val += mapping[l]
        return val
