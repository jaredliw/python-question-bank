class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Runtime: 57 ms
        # Memory: 13.4 MB
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        commons = []
        for item in nums1:
            if item in nums2:
                commons.append(item)
                nums2.remove(item)
        return commons
