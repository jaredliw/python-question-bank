class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        # Runtime: 28 ms
        # Memory: 13.5 MB
        p = list(range(1, m + 1))
        ans = []
        for q in queries:
            idx = p.index(q)
            ans.append(idx)
            p.pop(idx)
            p.insert(0, q)
        return ans
