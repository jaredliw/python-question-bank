class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Runtime: 24 ms
        # Memory: 13.6 MB
        ans = set()
        for idx1, word1 in enumerate(words):
            for idx2, word2 in enumerate(words):
                if idx1 != idx2 and word2 in word1:
                    ans.add(word2)
        return list(ans)
