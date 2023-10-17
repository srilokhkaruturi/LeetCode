# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        # Get the root value from postorder
        root_value = postorder.pop()
        # Create a new tree node with root_value
        root = TreeNode(root_value)
        
        # Find the index of root_value in inorder
        index = inorder.index(root_value)

        # Build the right subtree first, because we're popping from the end of postorder
        root.right = self.buildTree(inorder[index+1:], postorder)
        # Build the left subtree
        root.left = self.buildTree(inorder[:index], postorder)

        return root
