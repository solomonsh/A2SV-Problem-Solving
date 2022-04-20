def getPathsCount(graph,start,target):
        queue = [start]
        seen = set()
        path_length = 0

        while queue:
            
            for i in range(len(queue)):
                current = queue.pop(0)

                for neighbor in graph[current]:
                    if neighbor not in seen and  neighbor[1] == target:
                        return path_length+1
                    if neighbor not in seen:
                        queue.append(neighbor)
                        seen.add(current)
            path_length += 1      
            
            
        return path_length
    
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    
        unique_nodes = set(ids)
        if len(unique_nodes) == len(ids) or val not in ids:
            return -1

        graph = {}
        for i in range(graph_nodes):
            graph[(i+1),ids[i]] = []

        for j in range(len(graph_from)):
            graph[(graph_from[j],ids[graph_from[j]-1])].append((graph_to[j],ids[graph_to[j]-1]))
        
        for k in range(len(graph_to)):
            graph[(graph_to[k],ids[graph_to[k]-1])].append((graph_from[k],ids[graph_from[k]-1]))


        paths = []
        nodes = []

        for node in graph:
            if node[1] == val:
                nodes.append(node)
        
        for node in nodes:
            paths.append(getPathsCount(graph,node,val))
                
        return min(paths) if len(paths)>0 else -1


print(findShortest([5,4],[1,1,2,3],[2,3,4,5],[1,2,3,3,2],2))
