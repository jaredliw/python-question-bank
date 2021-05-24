from re import match


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Runtime: 2060 ms
        # Memory: 13.8 MB
        return match("^.*" + ".*".join(s) + ".*$", t) is not None


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Runtime: 20 ms
        # Memory: 13.5 MB
        ptr = 0
        for char in t:
            if ptr >= len(s):
                return True
            if s[ptr] == char:
                ptr += 1
        return ptr >= len(s)
