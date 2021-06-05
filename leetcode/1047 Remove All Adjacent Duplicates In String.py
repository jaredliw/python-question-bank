class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Runtime: 80 ms
        # Memory: 14.1 MB
        stack = []
        for char in s:
            if stack != [] and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
