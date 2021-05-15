class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        # Runtime: 16 ms
        # Memory: 13.5 MB
        number = number.replace(" ", "").replace("-", "")

        ans = ""
        length = len(number)
        cur = 0
        while length > 4:
            ans += number[cur:cur + 3]
            ans += "-"
            length -= 3
            cur += 3

        if length == 0:
            return ans[:-1]
        elif length == 4:
            return ans + number[cur:cur + 2] + "-" + number[cur + 2:]
        else:
            return ans + number[cur:]
