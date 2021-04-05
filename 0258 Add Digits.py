class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Runtime: 16 ms
        # Memory: 13.3 MB

        # Naive solution
        while num > 9:
            num = int(sum(map(int, str(num))))
        return num


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Runtime: 20 ms
        # Memory: 13.4 MB
        return 9 if num != 0 and num % 9 == 0 else num % 9
