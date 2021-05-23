class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 52 ms
        # Memory: 13.4 Mb
        return min(self.check(s, "0", "1"), self.check(s, "1", "0"))
        
    def check(self, string, char_even, char_odd):
        changes = 0
        for idx, char in enumerate(string):
            if idx % 2 == 0:
                if char != char_even:
                    changes += 1
            else:
                if char != char_odd:
                    changes += 1
        return changes
