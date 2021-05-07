class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        # Runtime: 12 ms
        # Memory: 13.8 Mb
        for idx, word in enumerate(sentence.split(), 1):
            if word.startswith(searchWord):
                return idx
        return -1
