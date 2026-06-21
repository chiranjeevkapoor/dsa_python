from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append(((i,j), 0))
                    visited[i][j] = 2
        
        tm = 0
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]

        while q:
            (r, c), t = q.popleft()
            tm = max(t, tm)
            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]
                if 0<=nrow<m and 0<=ncol<n and visited[nrow][ncol] != 2 and grid[nrow][ncol] == 1:
                    q.append(((nrow, ncol), t+1))
                    visited[nrow][ncol] = 2
        
        for i in range(m):
            for j in range(n):
                if visited[i][j] != 2 and grid[i][j] == 1:
                    return -1
        
        return tm

