 # Definition for a binary tree node.
from collections import deque
from os import curdir

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root):

        queue = deque([root])
        evenNodes = []
        grandChilds = []

        while queue:

            current = queue.popleft()
            if current.val%2 == 0:
                evenNodes.append(current)
            
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)
                 
        
        for node in evenNodes:
            if node.left:
                grandChilds += self.getGrandChilds(node.left)
            if node.right:
                grandChilds += self.getGrandChilds(node.right)

        return sum(grandChilds)
    
    def getGrandChilds(self,node):
        childs = []
        if node.left:
               childs.append(node.left.val)
        if node.right:
                childs.append(node.right.val)
        return childs






root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)

root.left.left = TreeNode(2)
root.left.right = TreeNode(7)

root.left.left.left = TreeNode(9)

root.left.right.left = TreeNode(1)
root.left.right.left = TreeNode(4)


root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(5)

sol = Solution()
print(sol.sumEvenGrandparent(root))