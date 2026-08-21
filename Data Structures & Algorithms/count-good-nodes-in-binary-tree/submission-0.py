# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # max value > curr

        def helper(node, x):
            if not node:
                return 0

            sol = 1 if node.val >= x else 0
            x = max(x, node.val)
            sol += helper(node.left, x)
            sol += helper(node.right, x)
            return sol

        return helper(root, root.val)
                