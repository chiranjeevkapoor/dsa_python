from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        ans = [[0 for _ in range(n)] for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visited[i][j] = 1
                    q.append(((i, j), 0))
        
        directions = [(-1, 0),(0,1),(1,0),(0,-1)]
        while q:
            (row, col), dist = q.popleft()
            ans[row][col] = dist

            for drow, dcol in directions:
                nrow = row + drow
                ncol = col + dcol
                if 0<=nrow<m and 0<=ncol<n and visited[nrow][ncol] == 0:
                    visited[nrow][ncol] = 1
                    q.append(((nrow, ncol), dist+1))
        
        return ans


        
                