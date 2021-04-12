class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # Runtime: 88 ms
        # Memory: 15.4 MB
        ans = "{"  # anyting > "z"
        for l in letters:
            if l > target:
                ans = min(ans, l)
        return letters[0] if ans == "{" else ans


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # Runtime: 84 ms
        # Memory: 15.3 MB
        try:
            return sorted(filter(lambda x: x > target, letters))[0]
        except:
            return letters[0]
