from collections import deque
 
class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        
        courses = {}
        indegree = {i:0 for i in range(numCourses)}

        for i in range(numCourses):
            courses[i] = []

        for c,p in prerequisites:
    
            courses[p].append(c)
            indegree[c] += 1
            
    

        queue = deque([])
        for course in courses:
            if indegree[course] == 0:
                queue.append(course)

        result = []
        while queue:
            cur = queue.popleft()
            result.append(cur)
            for child in courses[cur]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
            

        return (len(result) == numCourses)

sol = Solution()
        
sol.canFinish(2,[[1,0]])

# sol.canFinish(3,[[0,1],[0,2],[1,2]])
