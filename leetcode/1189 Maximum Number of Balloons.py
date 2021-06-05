class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # Runtime: 20 ms
        # Memory: 13.8 MB
        hashmap = {"a": 0, "b": 0, "l": 0, "o": 0, "n": 0}
        for char in text:
            if char in "balon":
                hashmap[char] += 1
        return min(min(hashmap["l"], hashmap["o"]) // 2, min(hashmap["b"], hashmap["a"], hashmap["n"]))
