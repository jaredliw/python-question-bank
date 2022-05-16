class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Runtime: 232 ms
        # Memory: 13.6 MB
        last = 0
        ptr = len(num) - 1
        while k != 0 or last != 0:
            if ptr < 0:
                num.add(0, 0)
                ptr = 0
            k, mod = divmod(k, 10)
            last, num[ptr] = divmod(num[ptr] + mod + last, 10)
            ptr -= 1
        return num
