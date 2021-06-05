class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # Runtime: 16 ms
        # Memory: 13.3 MB
        ans = []
        start = None
        last = None
        nums.append(99)  # Add a dummy number into nums
        for num in nums:
            if start is None:
                start = num
            elif num != last + 1:
                if last == start:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + "->" + str(last))
                start = num
            last = num
        return ans
