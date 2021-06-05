class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        # Runtime: 48 ms
        # Memory: 13.8 MB
        letters = {}
        for char in licensePlate:
            if char.isalpha():
                letters.setdefault(char.lower(), 0)
                letters[char.lower()] += 1

        match = ""
        for word in words:
            for letter, count in letters.items():
                if word.count(letter) < count:
                    break
            else:
                if match == "" or len(word) < len(match):
                    match = word
        return match
