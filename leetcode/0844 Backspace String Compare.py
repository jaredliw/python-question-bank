class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Rutnime: 20 ms
        # MemoryL: 13.4 MB
        final_s = self.convert(s)
        final_t = self.convert(t)
        return final_s == final_t

    def convert(self, string):
        char_arr = []
        for char in string:
            if char == "#":
                if char_arr:
                    char_arr.pop()
            else:
                char_arr.append(char)
        return char_arr
