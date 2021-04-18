class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        # Runtime: 16 ms
        # Memory: 13.6 MB
        return command.replace("()", "o").replace("(al)", "al")
