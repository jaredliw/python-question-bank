class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # Runtime: 16 ms
        # Memory: 13.6 MB
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        # Two-way hashmap
        seen_words = []
        seen_letters = []
        
        for idx, word in enumerate(words):
            if word in seen_words:
                if seen_letters[seen_words.index(word)] != pattern[idx]:
                    return False
            elif pattern[idx] in seen_letters:
                if seen_words[seen_letters.index(pattern[idx])] != word:
                    return False
            else:
                seen_words.append(word)
                seen_letters.append(pattern[idx])
        return True
