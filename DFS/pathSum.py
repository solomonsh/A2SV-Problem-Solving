# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):

        if root is None: return None
        def dfs(root,targetSum,sum=0):
            sum += root.val
            if sum == targetSum and root.left is None and root.right is None: 
                return True
            else:
                if root.left:
                    if dfs(root.left,targetSum,sum) is True:
                        return True
                
                if root.right: 
                    if dfs(root.right,targetSum,sum) is True:
                        return True

                return False
        return dfs(root,targetSum)


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(3)

# root.left.left = TreeNode(4)
# root.left.right = TreeNode(7)


sol = Solution()
print(sol.hasPathSum(root,5))

