class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Runtime: 172 ms
        # Memory: 14.7 MB
        last = arr[0]
        # Check for increasing
        for idx in range(1, len(arr)):
            if arr[idx] == last:
                return False
            elif arr[idx] < last:
                if idx == 1:  # arr is decreasing before increasing
                    return False
                else:
                    break
            last = arr[idx]
        else:  # arr is increasing without decreasing
            return False
        # Check for decreasing
        for idx1 in range(idx, len(arr)):
            if arr[idx1] == last:
                return False
            elif arr[idx1] > last:
                return False
            last = arr[idx1]
        return True
