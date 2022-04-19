from collections import deque

class Solution:
    def orangesRotting(self, grid):
      
        rottenOranges = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rottenOranges.append((i,j))
        
        queue = deque(rottenOranges)
        
        minutes = 0
        
        while queue:
            changed = False
            for i in range(len(queue)):
                current = queue.popleft()
                directions = [(0, 1), (1, 0), (-1, 0),(0, -1)]

                for d in directions:
                    new_row = current[0]+d[0]
                    new_col = current[1]+d[1]

                    if 0<= new_row<len(grid) and 0<= new_col < len(grid[0]) and  grid[new_row][new_col] == 1:
                        changed = True
                        grid[new_row][new_col] = 2
                        queue.append((new_row,new_col))
            if changed:
                 minutes += 1
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return minutes

sol = Solution()

print(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))    
print(sol.orangesRotting([[0]]))