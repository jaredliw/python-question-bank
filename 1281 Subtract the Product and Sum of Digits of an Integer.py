class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Runtime: 12 ms
        # Memory: 13.3 MB
        d_sum = 0
        d_prod = 1
        while n:
            n, digit_val = divmod(n, 10)
            d_sum += digit_val
            d_prod *= digit_val
        return d_prod - d_sum


from functools import reduce  # Remove this line in Python 2

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Python 2
        # Runtime: 20 ms
        # Memory: 13.5 MB

        # Python 3
        # Runtime: 24 ms
        # Memory: 14.1 MB
        return reduce(lambda total, item: total * int(item), str(n), 1) - reduce(lambda total, item: total + int(item),
                                                                                 str(n), 0)
