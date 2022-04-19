class Solution:
    def findCircleNum(self, isConnected):
       
        cities = [i for i in range(len(isConnected))]
        numberOfProcince = 0
       
                   
        def dfs(isConnected,current):
            
            n = len(isConnected)
          
            for i in range(n):
                if i in cities and isConnected[current][i] == 1:
                    cities.remove(i)
                    dfs(isConnected,current=i)
       
        while (len(cities)>0):
            
            numberOfProcince+=1
            city = cities.pop()
            dfs(isConnected,city)
    
        
        return numberOfProcince
sol = Solution()
print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
