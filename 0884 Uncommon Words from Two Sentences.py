from collections import Counter


class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        # Runtime: 20 ms
        # Memory: 13.4 MB
        ans = []
        for word, count in Counter(s1.split() + s2.split()).most_common():
            if count == 1:
                ans.append(word)
        return ans


class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        # Runtime: 12 ms
        # Memory: 13.5 MB
        seen_twice = set()
        unique = set()
        for word in s1.split() + s2.split():
            if word not in seen:
                if word in unique:
                    unique.remove(word)
                    seen_twice.add(word)
                else:
                    unique.add(word)
        return list(unique)
