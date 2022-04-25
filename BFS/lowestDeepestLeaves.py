# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root):
        
        parentsMapper = {root.val:None}

        queue = deque([root])
        previousLevelItems = [[root]]

        while queue:
            
            levelItems = []
            for q in range(len(queue)):
                current = queue.popleft()
                
                if current.left:
                    levelItems.append(current.left)
                    queue.append(current.left)
                    parentsMapper[current.left] = current
                
                if current.right:
                    levelItems.append(current.right)
                    queue.append(current.right)
                    parentsMapper[current.right] = current


            if len(levelItems) > 0:
                previousLevelItems[0] = levelItems
        


        deepestChild = previousLevelItems[0]
        lca = set()
        if len(deepestChild) == 1:
            return deepestChild[0]

        for i in deepestChild:
            lca.add(parentsMapper[i])
        
        if len(lca) == 1: return set(lsc).pop()

        paretnFound = False
        while not paretnFound:
            lsc = []
            for i in lca:
                lsc.append(parentsMapper[i])

            if len(set(lsc)) == 1:
                paretnFound = True

            lca = set(lsc)
        return set(lsc).pop()
    

