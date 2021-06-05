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
        # Runtime: 16 ms
        # Memory: 13.4 MB

        # Direct formula:
        #            r 0                        , if n = 0
        # dr_b(n) = <
        #            L 1 + ((n - 1) mod (b - 1)), if n != 0
        return 0 if num == 0 else (1 + (num - 1) % 9)


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Runtime: 20 ms
        # Memory: 13.4 MB

        # Direct formula:
        #            r 0            , if n = 0
        # dr_b(n) = <  b - 1        , if n != 0 and n congruent 0 (mod (b - 1))
        #            L n mod (b - 1), if n not congruent 0 (mod (b - 1))
        return 9 if num != 0 and num % 9 == 0 else num % 9
