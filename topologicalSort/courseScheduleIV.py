
from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites, queries):
        
        courses = {i:[] for i in range(numCourses)}
        isReachable = {i:[] for i in range(numCourses)}

        for pre,course in prerequisites:
            courses[pre].append(course)

        def bfs(start,target):
            visisted = set([start])
    
            queue = deque([start])
            
            while queue:
                cur = queue.popleft()

                if target in courses[cur]:
                    return start
                
                for child in courses[cur]:
            
                     if child not in visisted:  
                        queue.append(child)
                        visisted.add(child)

            return False
            
        result = []
        for i in range(numCourses):
                for j in range(numCourses):
                        isReach =  bfs(j,i)
                        if isReach is not False:
                            isReachable[i].append(isReach)
           
        for query in queries:
                result.append(True) if query[0] in isReachable[query[1]] else result.append(False)
           
        return result
        