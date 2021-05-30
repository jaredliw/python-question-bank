class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 16 ms
        # Memory: 13.5 MB
        max_score = 0
        count_1 = s.count("1")
        count_0 = 0
        for char in s[:-1]:
            if char == "0":
                count_0 += 1
            else:
                count_1 -= 1
            max_score = max(max_score, count_1 + count_0)
        return max_score
