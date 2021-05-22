class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # Runtime: 396 ms
        # Memory: 18.3 MB
        increasing = None
        for idx in range(len(A) - 1):
            if A[idx] < A[idx + 1]:
                if increasing is None:
                    increasing = True
                elif not increasing:
                    return False
            elif A[idx] > A[idx + 1]:
                if increasing is None:
                    increasing = False
                elif increasing:
                    return False
        return True
