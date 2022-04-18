class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
         
        if image[sr][sc] == newColor:
            return image
        
        row_length = len(image)
        col_length = len(image[0])
        
        directions = [(0, 1), (1, 0), (-1, 0),(0, -1)]
        
        target_color = image[sr][sc]
        image[sr][sc] = newColor
        
        for d in directions:
            new_row = sr+d[0]
            new_col = sc+d[1]
            
            if 0<=new_row<row_length and 0<=new_col<col_length and image[new_row][new_col] == target_color:
                
                self.floodFill(image,new_row,new_col,newColor)
                   
        return image
                
            