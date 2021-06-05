from functools import reduce  # Remove this line in Python 2


class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        # Runtime: 192 ms
        # Meory: 21 mB
        if ruleKey == "type":
            idx = 0
        elif ruleKey == "color":
            idx = 1
        else:
            idx = 2
        return reduce(lambda x, y: x + 1 if y[idx] == ruleValue else x, items, 0)
