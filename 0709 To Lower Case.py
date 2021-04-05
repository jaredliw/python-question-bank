class Solution(object):
    def toLowerCase(self, string):
        """
        :type string: str
        :rtype: str
        """
        # Runtime: 16 ms
        # Memory: 13.2 MB
        return string.lower()


class Solution(object):
    def toLowerCase(self, string):
        """
        :type string: str
        :rtype: str
        """
        return ''.join(chr(ord(c) + 32) if c >= 'A' and c <= 'Z' else c for c in string)