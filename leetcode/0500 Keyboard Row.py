class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Runtime: 16 ms
        # Memory: 13.4 MB
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        ans = []
        for word in words:
            for row in rows:
                if set(word.lower()).issubset(row):
                    ans.append(word)
                    break
        return ans
