# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # optimal dfs, we can keep track of visited count,
        # we know left is always min so no need for array
        count, sol = k, 0
        def helper(root):
            nonlocal count, sol
            if not root:
                return
            
            helper(root.left)
            if count == 0:
                return
            count -= 1
            if count == 0:
                sol = root.val
                return
            helper(root.right)
        
        helper(root)
        return sol