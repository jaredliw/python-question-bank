class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Runtime: 28 ms
        # Memory: 13.5 MB
        idx = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums2[n] > nums1[m]:
                nums1[idx] = nums2[n]
                n -= 1
            else:
                nums1[idx] = nums1[m]
                m -= 1
            idx -= 1

        while n >= 0:
            nums1[idx] = nums2[n]
            n -= 1
            idx -= 1


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Runtime: 28 ms
        # Memory: 13.3 MB
        nums1[:] = nums1[:m] + nums2
        nums1.sort()
