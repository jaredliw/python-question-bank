class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        # Runtime: 16 ms
        # Memory: 13.6 MB
        line_count = 1
        width_used = 0
        for char in s:
            char_len = widths[ord(char) - 97]
            if width_used + char_len <= 100:
                width_used += char_len
            else:
                line_count += 1
                width_used = char_len
        return line_count, width_used
