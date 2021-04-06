class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Runtime: 44 ms
        # Memory: 15.3 MB
        vowels = "aeiouAEIOU"
        s = list(s)
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] not in vowels:
                start += 1
            elif s[end] not in vowels:
                end -= 1
            else:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        return "".join(s)
