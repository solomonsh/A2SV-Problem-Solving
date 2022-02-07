
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
                
        level_sums = []
        
    
        queue = deque()
        queue.append(root)
        
        level_count = 0
        while queue:
            
            level_items = []
            for _ in range(len(queue)):
                current = queue.popleft()
                
                level_items.append(current.val)
                
                if current.left:
                    queue.append(current.left)
                
                if current.right:
                    queue.append(current.right)
                    
            level_count+=1
            level_sums.append((level_count,sum(level_items)))
            level_sums.sort()
             
        
        

        level_sums.sort(key=lambda  x: (x[1],-x[0]))
        return level_sums[-1][0]
                
        
        
        