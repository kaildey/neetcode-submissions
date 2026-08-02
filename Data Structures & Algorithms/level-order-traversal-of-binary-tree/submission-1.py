# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        count = 0
        goal = 1
        listCreate = []
        ans = []
        while queue:
            length = len(queue)

            for i in range(length):
                node = queue.popleft()
                listCreate.append(node.val)
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
            ans.append(listCreate)
            listCreate = []

        return ans