class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        # Runtime: 20 ms
        # Memory: 13.2 MB
        words = text.split()
        ans = []
        for idx in range(len(words) - 2):
            if words[idx] == first and words[idx + 1] == second:
                ans.append(words[idx + 2])
        return ans
