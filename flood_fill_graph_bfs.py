from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        q = deque()
        original_color = image[sr][sc]
        if original_color == color:
            return image
        
        q.append(((sr, sc), original_color))

        directions = [(-1, 0),(0, 1),(1, 0),(0,-1)]
        while q:
            (row, col), current_color = q.popleft()
            image[row][col] = color
            
            for drow, dcol in directions:
                nrow = row + drow
                ncol = col + dcol
                if 0<=nrow<n and 0<=ncol<m and image[nrow][ncol]==original_color:
                    q.append(((nrow, ncol), image[nrow][ncol]))
        
        return image