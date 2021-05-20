class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Runtime: 28 ms
        # Memory: 13.7 MB
        return self.hash(s) == self.hash(t)
    
    def hash(self, string):
        hashmap = {}
        max_id = 1
        ans = ""
        for char in string:
            if char not in hashmap:
                hashmap[char] = str(max_id)
                max_id += 1
            ans += hashmap[char]
        return ans
