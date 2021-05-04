class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Runtime: 20 ms
        # Memory: 13.4 MB
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        unique = set()
        for word in words:
            string = ""
            for char in word:
                string += morse[ord(char) - 97]
            unique.add(string)
        return len(unique)
