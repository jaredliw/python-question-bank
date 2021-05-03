class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Runtime: 16 ms
        # Memory: 13.6 MB
        for idx in range(1, len(s), 2):
            s = s[:idx] + chr(ord(s[idx - 1]) + int(s[idx])) + s[idx + 1:]
        return s
   
