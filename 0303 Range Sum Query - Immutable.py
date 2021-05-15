class NumArray(object):
    # Runtime: 68 ms
    # Memory: 17 MB
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix_sum = []
        last = 0
        for num in nums:
            last += num
            self.prefix_sum.append(last)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] - self.prefix_sum[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
