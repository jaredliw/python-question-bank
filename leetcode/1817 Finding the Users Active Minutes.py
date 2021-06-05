class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # Runtime: 948 ms
        # Memory: 22.2 MB
        ans = [0] * k
        hashmap = {}
        for uid, uam in logs:
            hashmap.setdefault(uid, set())
            hashmap[uid].add(uam)

        for time in hashmap.values():
            ans[len(time) - 1] += 1
        return ans
