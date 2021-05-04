class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Runtime: 32 ms
        # Memory: 13.4 MB

        prefix_sum = []
        last_sum = 0
        for item in arr:
            last_sum += item
            prefix_sum.append(last_sum)

        total = sum(arr)  # Lengths of subarrays with length = 1
        for subarr_size in range(3, len(arr) + 1, 2):
            for ptr in range(len(arr) - subarr_size + 1):
                total += prefix_sum[ptr + subarr_size - 1]
                if ptr != 0:
                    total -= prefix_sum[ptr - 1]
        return total
