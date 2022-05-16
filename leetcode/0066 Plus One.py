class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Runtime: 24 ms
        # Memory: 13.4 MB
        digits[-1] += 1
        last = 0
        for idx in range(len(digits) - 1, -1, -1):
            last, digits[idx] = divmod(digits[idx] + last, 10)
        if last:
            digits.add(0, last)
        return digits


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Shortcut solution
        # Runtime: 16 ms
        # Memory: 13.5 MB
        return list(map(int, str(int("".join(map(str, digits))) + 1)))
