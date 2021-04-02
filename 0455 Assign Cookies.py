class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # Runtime: 140 ms
        # Memory: 15.2 MB
        g.sort()
        s.sort()
        child_idx = 0
        cookie_idx = 0
        while child_idx < len(g) and cookie_idx < len(s):
            if s[cookie_idx] >= g[child_idx]:
                child_idx += 1
            cookie_idx += 1
        return child_idx