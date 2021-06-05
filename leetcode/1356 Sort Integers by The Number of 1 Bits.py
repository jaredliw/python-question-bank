class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Runtime: 52 ms
        # Memory: 13.7 MB
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))
