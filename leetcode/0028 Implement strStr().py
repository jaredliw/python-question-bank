class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Runtime: 20 ms
        # Memory: 13.7 MB
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        # One thing to take note here is if needle="" the condition will be True and str.index() will return 0
