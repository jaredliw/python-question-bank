class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 48 ms
        # Memory: 13.6 MB
        max_len = 0
        occr = ""
        for tail_idx, char in enumerate(s):
            if char in occr:
                max_len = max(max_len, len(occr))
                occr = occr[occr.index(char) + 1:]
            occr += char
        max_len = max(max_len, len(occr))
        return max_len
