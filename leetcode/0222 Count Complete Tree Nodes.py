
# BFS: O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Runtime: 339 ms
        # Memory: 29.8 MB
        to_visit = [root]
        visited = set()
        while to_visit:
            node = to_visit.pop(0)
            if node in visited or node is None:
                continue
            visited.add(node)
            to_visit.append(node.left)
            to_visit.append(node.right)
        return len(visited)
