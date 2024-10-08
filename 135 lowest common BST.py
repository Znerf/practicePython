# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def return_path(rt:'Treenode', target:'Treenode')->'Array[Treenode]':
            path=[]
            while rt:
                path.append(rt)
                # print(rt.val)
                if rt.val == target.val:
                    return path
                # print(rt.val)
                if target.val > rt.val:
                    rt=rt.right
                else:
                    rt=rt.left
            return path



        common = root
        
        pathp=return_path(root,p)
        pathq=return_path(root,q)
        # print([x.val for x in pathq])
        a = pathp if len(pathp)>=len(pathq) else pathq
        b = pathp if len(pathp)<len(pathq) else pathq

        print([x.val for x in b])
        for index, path in enumerate(b):
            print(path.val, a[index].val)
            if path != a[index]:
                # print("dsf",a[index-1].val)
                return a[index-1]
        return b[-1]
