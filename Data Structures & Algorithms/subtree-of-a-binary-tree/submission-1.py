# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.check = False
        self.checkLittle = True

    def checker(self, root, subRoot):
        if root is None and subRoot is None:
            return

        if root is None and subRoot is not None:
            self.checkLittle = False
            return
        
        if root is not None and subRoot is None:
            self.checkLittle = False
            return
        
        if root.val != subRoot.val:
            self.checkLittle = False
            return

        self.checker(root.left, subRoot.left)
        self.checker(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return

        self.checkLittle = True
        self.checker(root, subRoot)

        if self.checkLittle:
            self.check = True
            
        self.isSubtree(root.left, subRoot)
        self.isSubtree(root.right, subRoot)

        return self.check
