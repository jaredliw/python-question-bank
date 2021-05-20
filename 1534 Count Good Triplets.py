class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        # Runtime: 1472 ms
        # Memory: 13.5 MB
        length = len(arr)
        count = 0
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    if i < j < k and abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(
                            arr[i] - arr[k]) <= c:
                        count += 1
        return count
