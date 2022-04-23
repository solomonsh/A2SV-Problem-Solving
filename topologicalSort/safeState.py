from collections import deque

class Solution:
    def eventualSafeNodes(self, graph):
        
        terminated_nodes = [i for i in range(len(graph)) if len(graph[i]) == 0 ]
        
        adjList = {i:[] for i in range(len(graph))}
        for i,child in enumerate(graph):
            for c in child:
                adjList[c].append(i)
        
        queue = deque(terminated_nodes)
        while queue:
            current = queue.popleft()

            if len(graph[current]) == 0:
                pass


sol = Solution()
sol.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])