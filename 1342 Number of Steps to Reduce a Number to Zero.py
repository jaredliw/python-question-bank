class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Runtime: 20 ms
        # Memory: 13.5 MB
        n_step = 0
        while num != 0:
            if num % 2:
                num -= 1
            else:
                num >>= 1
            n_step += 1
        return n_step
