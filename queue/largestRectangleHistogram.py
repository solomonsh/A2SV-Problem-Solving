class Solution:
    def largestRectangleArea(self, heights):
        
        stack = []
        max_area  = 0
        
        for i,n in enumerate(heights):
            
            start = i
            
            while stack and stack[-1][1] >= n:
                
                popped_value = stack.pop()
                
                new_area = popped_value[1]*(i-popped_value[0])
                
                max_area = max(max_area,new_area)
                
                start = popped_value[0]
            
            stack.append([start,n])
            
         
        for s in stack:
            
            new_area = (len(heights)-s[0])*s[1]
            
              
            max_area = max(max_area,new_area)
            
        return max_area