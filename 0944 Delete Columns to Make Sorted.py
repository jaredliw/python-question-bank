class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        # Runtime: 208 ms
        # Memory: 15.1 MB
        count = 0
        for col in zip(*strs):
            for idx in range(1, len(col)):
                if col[idx] < col[idx - 1]:
                    count += 1
                    break
        return count


class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        # Runtime: 168 ms
        # Memory: 14.6 MB
        count = 0
        for col in range(len(strs[0])):
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row - 1][col]:
                    count += 1
                    break
        return count
