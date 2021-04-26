class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # Runtime: 672 ms
        # Memory: 52.7 MB
        
        # Any two edges must have a common node, which is the center. (Since the maximum depth of the star graph is 1)
        return set(edges[0]).intersection(set(edges[1])).pop()
