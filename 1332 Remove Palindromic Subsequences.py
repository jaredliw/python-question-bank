class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 13 ms
        # Memory: 13.3 MB

        # If s is a palindrome, we just need one step.
        if s == s[::-1]:
            return 1
        # Subsequences composed of only one type of letter are always palindrome strings.
        else:
            return 2
