# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.check = True

    def checker(self, p, q):
        if not p or not q:
            if not p and not q:
                return
            else:
                self.check = False
                return

        if p.val != q.val:
            self.check = False

        self.checker(p.left, q.left)
        self.checker(p.right, q.right)
        return self.check

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p:
            return True if not q else False
        if not q:
            return False

        return self.checker(p, q)