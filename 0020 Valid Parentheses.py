class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Runtime: 16 ms
        # Memory: 13.4 MB
        matches = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for p in s:
            if p in "([{":
                stack.append(p)
            elif not stack:
                return False
            elif matches[stack[-1]] == p:
                stack.pop(-1)
            else:
                return False
        return not stack
