from collections import Counter


class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Runtime: 48 ms
        # Memory: 13.7 MB
        max_match = -1
        for num, count in Counter(arr).most_common():
            if num == count:
                max_match = max(max_match, num)
        return max_match


class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Runtime: 44 ms
        # Memory: 13.5 MB
        counter = {}
        for num in arr:
            counter.setdefault(num, 0)
            counter[num] += 1
        
        max_match = -1
        for num, count in counter.items():
            if num == count:
                max_match = max(max_match, num)
        return max_match
