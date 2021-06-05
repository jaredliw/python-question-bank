class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Runtime: 96 ms
        # Memory: 14.9 MB
        biggest = -1
        ans = []
        for item in arr[::-1]:
            ans.append(biggest)
            biggest = max(biggest, item)
        return ans[::-1]
