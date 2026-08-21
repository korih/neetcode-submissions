# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(root):
            if not root:
                return [True, 0]

            left = helper(root.left)
            right = helper(root.right)
            if not left[0] or not right[0]:
                return [False, 0]
            val = abs(left[1] - right[1])
            if val > 1:
                return [False, val]
            
            return [True, max(left[1], right[1]) + 1]



        return helper(root)[0]