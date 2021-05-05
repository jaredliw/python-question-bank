class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Runtime: 12 ms
        # Memory: 13.5 MB

        # Scan from right to left is a better way to solve this
        string = ""
        idx = len(s) - 1
        while idx >= 0:
            if s[idx] == "#":
                string += chr(int(s[idx - 2: idx]) + 96)
                idx -= 3
            else:
                string += chr(int(s[idx]) + 96)
                idx -= 1
        return string[::-1]
