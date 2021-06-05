class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Runtime: 20 ms
        # Memory: 13.5 MB
        count = 0
        for idx, char in enumerate(s):
            if char in "aeiouAEIOU":
                if idx < len(s) // 2:
                    count += 1
                else:
                    count -= 1
        return count == 0
