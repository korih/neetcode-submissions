# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal, get list
        # value index?
        sol = []

        def helper(root, counter):
            if not root:
                return
            
            helper(root.left, counter)
            counter.append(root.val)
            helper(root.right, counter)
            return
        
        helper(root, sol)
        return sol[k - 1]

