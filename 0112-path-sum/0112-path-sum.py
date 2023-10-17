# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, root.val)]
        
        while stack:
            current, current_sum = stack.pop()
            
            # check if at rootnode
            if not current.left and not current.right:
                if current_sum == targetSum:
                    return True
            
            if current.left:
                stack.append((current.left, current.left.val + current_sum))
            if current.right:
                stack.append((current.right, current.right.val + current_sum))
                
        return False