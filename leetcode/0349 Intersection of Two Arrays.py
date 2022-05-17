class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Runtime: 36 ms
        # Memory: 13.7 MB
        return list(set(nums1).intersection(set(nums2)))
