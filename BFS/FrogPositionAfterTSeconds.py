from collections import deque

class Solution:
    def frogPosition(self, n, edges, t, target):
        tree = {0:[[1,1],1]}

        for e in edges:
            if e[0] in tree:
                tree[e[0]][0]+= [e[1]]
            else:
                tree[e[0]] = [[e[1]],1]

            if e[1] in tree:
                tree[e[1]][0]+= [e[0]]
            else:
                tree[e[1]] = [[e[0]],1]
        
    
        if len(edges) == 0 and target == 1:
            return 1.0
        elif len(edges) == 0:
            return 0
        
        if target not in tree:
            return 0
        
        tree[1][0].append(0)
        
        queue = deque([(1,0,0)])

        visisted = {0,1}

        while queue:

            current = queue.popleft()
            parent = current[2]

            parentProb = tree[parent][1]
            parentChilds = len(tree[parent][0])-1

            curProb = parentProb*(1/parentChilds)
            
            tree[current[0]] = [tree[current[0]][0],curProb]

            if current[0] == target:
                if t == current[1]:
                    return curProb
                elif t > current[1] and len(tree[current[0]][0])==1:
                    return curProb
                
            for child in tree[current[0]][0]:
                if child not in visisted:
                    queue.append((child,current[1]+1,current[0]))
                    visisted.add(child)
        return 0.0
 
sol = Solution()
print(sol.frogPosition(9,[[2,1],[3,1],[4,2],[5,1],[6,2],[7,5],[8,7],[9,7]],6,8))