class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        # Runtime: 20 ms
        # Memory: 13.3 MB
        return self.to_num(firstWord) + self.to_num(secondWord) == self.to_num(targetWord)
        
    def to_num(self, string):
        ans = 0
        for char in string:
            ans *= 10
            ans += ord(char) - 97
        return int(ans)
