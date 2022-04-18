# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt  = 0
        
        def valueSum(root):
            
            if root is None:
                return 0
            
            left_sum = valueSum(root.left)

            right_sum = valueSum(root.right)

            self.total_tilt += abs(left_sum - right_sum)

            return left_sum + right_sum + root.val
        
        valueSum(root)
        
        return self.total_tilt
        
        
        