from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root):

        queue = deque([root])
        if root is None: return []
        
        order = 1
        result = []
       
        while queue:
            
            level_items = []
            for q in range(len(queue)):
                
                current = queue.popleft()
                
                if current.left:
                    queue.append(current.left)
                
                if current.right:
                    queue.append(current.right)

                level_items.append(current.val)
            
            if order == 1:
                result.append(level_items) 

            else:
                level_items.reverse()
                result.append(level_items)

            order *= -1
        
        return result
                    

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)


root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
        

sol = Solution()
print(sol.zigzagLevelOrder(root))
                    
                


                


