class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        # Runtime: 16 ms
        # Memory: 13.4 MB
        S = S.split()
        for idx, word in enumerate(S):
            if word[0] in "aeiouAEIOU":
                S[idx] = word + "ma" + "a" * (idx + 1)
            else:
                S[idx] = word[1:] + word[0] + "ma" + "a" * (idx + 1)
        return " ".join(S)
