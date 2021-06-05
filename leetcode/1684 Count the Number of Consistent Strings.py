class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        # Runtime: 212 ms
        # Memory: 15.7 MB
        count = 0
        allowed = set(allowed)
        for w in words:
            if set(w).issubset(allowed):
                count += 1
        return count
