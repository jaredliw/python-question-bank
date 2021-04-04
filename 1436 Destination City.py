class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        # Runtime: 32 ms
        # Memory: 13.6 MB
        starts = map(lambda x: x[0], paths)
        return list(filter(lambda x: x not in starts, map(lambda x: x[1], paths)))[0]


class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        hashmap = {}
        for start, end in paths:
            hashmap[start] = end
        destination = paths[0][0]
        while True:
            try:
                destination = hashmap[destination]
            except:
                break
        return destination