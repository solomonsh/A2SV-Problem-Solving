from collections import deque 
 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root):

        queue = deque([root])

        while queue:

            level_items = []

            for q in range(len(queue)):
                current = queue.popleft()

                if current.left: 
                    queue.append(current.left)
                    level_items.append(current.left.val)

                else: 
                   level_items.append(None)

                if current.right: 
                    queue.append(current.right)
                    level_items.append(current.right.val)

                else: 
                  level_items.append(None)

              
            level_left = level_items[:len(level_items)//2]
            level_right = level_items[len(level_items)//2:]
            level_right.reverse()

            if len(level_items) == 1: continue
    
            elif level_left != level_right:
                    return False
                
        return True




root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(2)

# root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
    

# root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
        

sol = Solution()
print(sol.isSymmetric(root))
                    
                


                



        