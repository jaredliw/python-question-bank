class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Runtime: 44 ms
        # Memory: 14.8 MB
        return sorted(s) == sorted(t)


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Runtime: 36 ms
        # Memory: 14.6 MB

        # Slightly improvements from the previous solution:
        # We check for lengths first, if they are not the same, then t can't be an anagram of s
        # Due to short circuit evaluation, the second condition will not be tested if the first condition is false
        return len(s) == len(t) and sorted(s) == sorted(t)
