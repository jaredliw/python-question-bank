class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Runtime: 20 ms
        # Memory: 13.6 MB
        counter = {}
        for num in arr:
            counter.setdefault(num, 0)
            counter[num] += 1

        return len(set(counter.values())) == len(counter.values())
