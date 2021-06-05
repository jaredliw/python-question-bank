class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        # Runtime: 24 ms
        # Memory: 13.4 MB

        # In Python 2, you need to convert the divisor/dividend into float in order to get a float answer
        return (sum(salary) - min(salary) - max(salary)) / float(len(salary) - 2)
