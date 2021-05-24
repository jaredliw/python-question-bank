class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Runtime: 32 ms
        # Memory: 13.4 MB
        for idx in range(len(arr) - 2):
            if arr[idx] % 2 == 1 and arr[idx + 1] % 2 == 1 and arr[idx + 2] % 2 == 1:
                return True
        return False
