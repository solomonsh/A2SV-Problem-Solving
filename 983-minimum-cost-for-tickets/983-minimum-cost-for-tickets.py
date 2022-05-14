class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        memo = {}  
        def getIndex(index,day):
            j = 1
            while j<len(days) and days[j] < day:
                j += 1
            
            return j
           
            
        def dfs(index):
            if index>= len(days):
                return 0
            
            if index in memo:
                return memo[index]
            
            path1 = getIndex(index,days[index] + 1)
            path2 = getIndex(index,days[index] + 7)  
            path3 = getIndex(index,days[index] + 30) 			
            
            print(path1,path2,path3)
            result = min(costs[0] + dfs(path1),costs[1] + dfs(path2),costs[2] + dfs(path3))
            memo[index] = result 
            return memo[index]
                                                 
        return dfs(0)