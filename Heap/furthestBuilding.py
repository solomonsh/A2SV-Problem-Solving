class Solution:
    def furthestBuilding(self, heights , bricks, ladders):
        
        diffs = []
        for i in range(len(heights)-1):
            if heights[i+1] - heights[i] > 0:
                diffs.append(heights[i+1] - heights[i])
            
        total_bricks = ladders*max(diffs)+bricks
        
        furthest = 0
        index = 0
        for i in range(len(heights)-1):
            index = i
            
            if furthest > total_bricks:
                return i-1
            
            if heights[i+1] - heights[i] > 0:
                    furthest+= heights[i+1] - heights[i]
        
        if furthest > total_bricks:
            return index
        else:
            return len(heights)-1
            

sol = Solution()

# print(sol.furthestBuilding([4,12,2,7,3,18,20,3,19],10,2))

print(sol.furthestBuilding([14,3,19,3],17,0))
