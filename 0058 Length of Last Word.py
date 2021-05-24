class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 12 ms
        # Memory: 13.6 MB
        words = s.split()
        if not words:
            return 0
        else:
            return len(words[-1])


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 20 ms
        # Memory: 13.4 MB
        try:
            return len(s.split()[-1])
        except IndexError:
            return 0
