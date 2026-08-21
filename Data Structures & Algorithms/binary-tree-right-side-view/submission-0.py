# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        sol = []

        def helper(root, height):
            if not root:
                return None
            if len(sol) == height:
                sol.append(root.val)
            
            helper(root.right, height + 1)
            helper(root.left, height + 1)
            
        helper(root, 0)
        return sol
