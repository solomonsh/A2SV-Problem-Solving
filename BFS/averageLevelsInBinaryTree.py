# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root):

        queue = deque([root])
        result = []

        while queue:
            level_items =  []

            for q in range(len(queue)):

                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                    
                if current.right:
                    queue.append(current.right)

                level_items.append(current.val)

            result.append(sum(level_items)/len(level_items))
          

        return result
    

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)


root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
        

sol = Solution()
print(sol.averageOfLevels(root))