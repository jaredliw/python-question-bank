class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 100 ms
        # Memory: 16.1 MB
        distinct = set(nums)
        return 2 * sum(distinct) - sum(nums)


from functools import reduce  # Do not need this line in python 2

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Python 3:
        # Runtime: 136 ms
        # Memory: 16.8 MB

        # Python 2:
        # Runtime: 124 ms
        # Memory: 15.6 MB
        return reduce(lambda accum, item: int(accum) ^ int(item), nums)


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 112 ms
        # Memory: 16.3 MB

        # I have tested to use a list for hashset, here is the result:
        # Runtime: 904 ms
        # Memory: 15.6 MB
        hashset = set()
        for item in nums:
            if item not in hashset:
                hashset.add(item)
            else:
                hashset.remove(item)
        # The "lonely" element will be the only item in the set
        return list(hashset)[0]


from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 132 ms
        # Memory: 16.7 MB
        return Counter(nums).most_common()[-1][0]
