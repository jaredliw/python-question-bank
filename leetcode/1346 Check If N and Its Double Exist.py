class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Runtime: 36 ms
        # Memory: 13.4 MB
        hashset = set()
        for num in arr:
            if num % 2 == 0:
                if num // 2 in hashset:
                    return True
            if num * 2 in hashset:
                return True
            hashset.add(num)
        return False
