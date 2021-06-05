class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Runtime: 44 ms
        # Memory: 13.9 MB
        magazine = list(magazine)
        try:
            [magazine.remove(char) for char in ransomNote]
            return True
        except ValueError:
            return False
