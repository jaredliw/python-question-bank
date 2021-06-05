class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        # Runtime: 20 ms
        # Memory: 13.5 MB
        ans = []
        start = 0
        s += "#"  # Dummy char
        for idx, char in enumerate(s):
            if char != s[start]:
                if idx - start >= 3:
                    ans.append([start, idx - 1])
                start = idx
        return ans
