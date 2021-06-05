from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 152 ms
        # Memory: 15 MB
        return Counter(nums).most_common(1)[0][0]


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 132 ms
        # Memory: 14.8 MB
        hashmap = {}
        for item in nums:
            hashmap.setdefault(item, 0)
            hashmap[item] += 1
        return max(hashmap.items(), key=lambda x: x[1])[0]


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 136 ms
        # Memory: 15.1 MB

        # Boyer–Moore Majority Vote Algorithm
        major = None
        count = 0
        for num in nums:
            if count == 0:
                major = num
                count += 1
            elif num == major:
                count += 1
            else:
                count -= 1
        return major
