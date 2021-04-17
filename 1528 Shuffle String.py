class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        # Runtime: 48 ms
        # Memory: 13.5 MB
        return "".join(map(lambda x: x[1], sorted(zip(indices, s))))


class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        # Runtime: 64 ms
        # Memory: 13.4 Mb
        ans = [""] * len(s)
        for char, idx in zip(s, indices):
            ans[idx] = char
        return "".join(ans)
