class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # Runtime: 20 ms
        # Memory: 13.3 MB
        if len(s) != len(goal):
            return False
        return goal in (s + s)


class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # Runtime: 12 ms
        # Memory: 13.5 MB
        if s == goal == "":
            return True
        
        for idx in range(len(goal)):
            if s[idx:] + s[:idx] == goal:
                return True
        return False
