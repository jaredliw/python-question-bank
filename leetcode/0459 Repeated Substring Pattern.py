class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Runtime: 40 ms
        # Memory: 14 MB
        s_length = len(s)
        for length in range(1, s_length):
            if s_length % length == 0:
                substring = s[:length] * (s_length // length)
                if substring == s:
                    return True
        return False
