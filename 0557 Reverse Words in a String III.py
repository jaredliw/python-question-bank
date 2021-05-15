class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Runtime: 16 ms
        # Memory: 14.6 MB
        s = s.split()
        ans = []
        for word in s:
            ans.append(word[::-1])
        return " ".join(ans)
