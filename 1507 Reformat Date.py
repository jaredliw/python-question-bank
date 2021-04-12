class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        # Runtime: 12 ms
        # Memory: 13.5 MB
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        d, m, y = date.split()
        return "{}-{:0>2}-{:0>2}".format(y, months.index(m) + 1, d[:len(d)//2])
