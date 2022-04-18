 
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = []
 
class Solution:
 
    def maxDepth(self, root: 'Node') -> int:
        self.maxDep = 0

        def dfs(root,depth = 0):
            if root is None:
                return None
            depth += 1
            self.maxDep = max(self.maxDep,depth)

            for child in root.children:
                dfs(child,depth)
            

        dfs(root)
        return self.maxDep
    
        

root = Node(1)
node2 = Node(2)


node3 = Node(3)
node3.children.append(Node(6))

node4 = Node(4)


root.children.append(node2)
root.children.append(node3)
root.children.append(node4)

sol = Solution()
print(sol.maxDepth(root))

