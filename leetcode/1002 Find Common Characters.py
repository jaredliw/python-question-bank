from collections import Counter


class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Runtime: 59 ms
        # Memory: 13.8 MB
        chars = dict(Counter(words[0]))
        for word in words[1:]:
            for char, count in chars.items():
                chars[char] = min(word.count(char), count)
                if chars[char] == 0:
                    del chars[char]

        commons = []
        for char, count in chars.items():
            commons.extend([char] * count)
        return commons
