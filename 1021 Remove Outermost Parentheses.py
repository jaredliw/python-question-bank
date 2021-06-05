class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Runtime: 28 ms
        # Memomry: 13.6 MB
        stack = 0
        ans = ""
        for char in s:
            if char == "(":
                if stack != 0:
                    ans += char
                stack += 1
            else:
                if stack != 1:
                    ans += char
                stack -= 1
        return ans
