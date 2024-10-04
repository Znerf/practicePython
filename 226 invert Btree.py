# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root:
        #     return root

        # start = root
        # newNode = start

        # def rec(node , finalNode):
        #     print(start)
        #     print()
        #     if node.left and node.right:
        #         # print(node.left ,node.right)
        #         finalNode.right = node.left
        #         finalNode.left = node.right

        #         rec(node.left, finalNode.right )
        #         rec(node.right, finalNode.left )
        #     else:
        #         finalNode.right = None
        #         finalNode.left = None

        #     return
        # rec(root,newNode)

        # return newNode'

        if not root:
            return
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
            

        





        