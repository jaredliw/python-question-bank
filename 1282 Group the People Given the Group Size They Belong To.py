class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        # Runtime: 64 ms
        # Memory: 13.6 MB
        hashmap = {}
        groups = []
        for idx, size in enumerate(groupSizes):
            hashmap.setdefault(size, [])
            # If the group is full, open a new one
            if len(hashmap[size]) == size:
                groups.append(hashmap[size])
                hashmap[size] = []
            # All numbers in a group must be the same
            hashmap[size].append(idx)
        groups.extend(hashmap.values())
        return groups
