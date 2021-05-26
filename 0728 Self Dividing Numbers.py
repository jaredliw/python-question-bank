class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # Runtime: 40 ms
        # Memory: 13.3 MB
        ans = []
        for num in range(left, right + 1):
            for divisor in str(num):
                if divisor == "0" or num % int(divisor) != 0:
                    break
            else:
                ans.append(num)
        return ans
