from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        
        queue = deque([root])
        result = []

        while queue:
            
            level_items = []
            for q in range(len(queue)):
                
                current = queue.popleft()
                level_items.append(current.val)

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)
                
            result.append(level_items[-1])

        return result




