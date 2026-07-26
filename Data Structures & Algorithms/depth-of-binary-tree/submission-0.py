# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max: int = 0
        self.count: int = 0

    def counter(self, root):
        if not root:
            self.max = max(self.max, self.count)
            return
        
        self.count += 1
        self.counter(root.left)
        self.counter(root.right)
        self.count -= 1

        return self.max

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return self.max
        return self.counter(root)
        