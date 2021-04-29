class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Runtime: 24 ms
        # Memory: 13.6 MB
        arr.sort()
        diffs = list(map(lambda idx: arr[idx] - arr[idx - 1], range(1, len(arr))))
        return len(diffs) == diffs.count(diffs[0])  # Check if all elements are same
