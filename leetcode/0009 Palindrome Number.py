class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Runtime: 40 ms
        # Memory: 13.4 MB
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Runtime: 60 ms
        # Memory: 13.3 MB

        # Pure math solution
        if x < 0:
            return False
        original_num = x
        reversed_num = 0
        # Same concept as #7
        while x != 0:
            reversed_num *= 10
            reversed_num += x % 10
            x //= 10
        return original_num == reversed_num
