# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.vals = []
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Runtime: 24 ms
        # Memory: 13.3 MB

        # Recursive
        if root is not None:
            if root.left is not None:
                self.inorderTraversal(root.left)
            self.vals.append(root.val)
            if root.right is not None:
                self.inorderTraversal(root.right)
        return self.vals


