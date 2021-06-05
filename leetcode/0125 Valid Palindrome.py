# Python 2 only
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Runtime: 28 ms
        # Memory: 14.2 MB
        alnum = filter(str.isalnum, str(s.lower()))
        return alnum == alnum[::-1]


# Python 3 only
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Runtime: 36 ms
        # Memory: 15.7 MB
        alnum = list(filter(str.isalnum, s.lower()))  # you can't convert it to str directly
        return alnum == alnum[::-1]
