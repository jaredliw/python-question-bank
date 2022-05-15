from itertools import zip_longest


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Runtime: 39 ms
        # Memory: 13.9 MB
        for idx in range(1, len(words)):
            for char1, char2 in zip_longest(words[idx - 1], words[idx], fillvalue=''):
                index1 = order.index(char1) if char1 != '' else -1
                index2 = order.index(char2) if char2 != '' else -1
                print(char1, index1, char2, index2)
                if index1 > index2:
                    return False
                elif index1 < index2:
                    break
        return True
