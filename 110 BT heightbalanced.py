# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dp(node,height):
            if node == None: return height-1
            left = dp(node.left, height+1)
            right = dp(node.right, height+1)
            return -1 if left<0 or right<0 or abs(left-right) >1  else max(left,right)
        return root == None or dp(root,0)>=0
