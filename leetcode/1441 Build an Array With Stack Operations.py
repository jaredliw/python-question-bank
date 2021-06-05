class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        # Runtime: 12 ms
        # Meomory: 13.4 Mb
        ptr = 0
        ans = []
        for num in range(1, n + 1):
            if max(target) < num:
                break
            elif num in target:
                ans.append("Push")
            else:
                ans.extend(["Push", "Pop"])
        return ans
