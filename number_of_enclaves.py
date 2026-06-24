from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[0 for _ in range(m)] for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if i==0 or i==n-1 or j==0 or j==m-1:
                    if grid[i][j]==1:
                        q.append((i, j))
                        visited[i][j] = 1
        
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        while q:
            row, col = q.popleft()
            

            for drow, dcol in directions:
                nrow = row + drow
                ncol = col + dcol
                if 0<=nrow<n and 0<=ncol<m and grid[nrow][ncol]==1 and visited[nrow][ncol] == 0:
                    q.append((nrow, ncol))
                    visited[nrow][ncol] = 1
        
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and visited[i][j]==0:
                    count+=1
        return count




        