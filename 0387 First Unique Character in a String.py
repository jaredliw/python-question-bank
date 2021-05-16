from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 216 ms
        # Memory: 13.8 MB
        counter = Counter(s)
        for idx, char in enumerate(s):
            if counter[char] == 1:
                return idx
        return -1


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 160ms
        # Memory: 13.8 MB
        seen = {}
        for char in s:
            seen.setdefault(char, 0)
            seen[char] += 1
        for idx, char in enumerate(s):
            if seen[char] == 1:
                return idx
        return -1
