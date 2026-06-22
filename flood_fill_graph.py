class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
        self.dfs(sr, sc, original_color, color, image)

        return image
    
    def dfs(self, row, col, original_color, color, image):
        n = len(image)
        m = len(image[0])
        if row<0 or row>=n or col<0 or col>=m:
            return
        if image[row][col] != original_color:
            return
        image[row][col] = color
        directions = [(0,-1),(-1,0),(0,1),(1,0)]

        for drow, dcol in directions:
            nrow = row + drow
            ncol = col + dcol
            self.dfs(nrow, ncol, original_color, color, image)




        
        