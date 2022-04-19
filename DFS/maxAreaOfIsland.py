class Solution:
    def maxAreaOfIsland(self, grid):
        
        self.lands = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.lands.append((i,j))
          
        self.count = 0
        def dfs(grid,current):
            self.count +=1
            directions = [(0, 1), (1, 0), (-1, 0),(0, -1)]
            grid[current[0]][current[1]] = 0
            for d in directions:
                new_row = current[0]+d[0]
                new_col = current[1]+d[1]
                
                if 0<=new_row<len(grid) and 0<=new_col<len(grid[0]) and grid[new_row][new_col] == 1:
                    self.lands.remove((new_row,new_col))
                    dfs(grid,(new_row,new_col))

         
        
        areas = []
        
        for land in self.lands:
            self.count = 0
            dfs(grid,land)
            areas.append(self.count)
     
        return max(areas)
 