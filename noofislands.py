from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        n = len(grid)
        m = len(grid[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]
        for row in range(n):
            for col in range(m):
                if visited[row][col] == 0 and grid[row][col] == '1':
                    self.bfs(row, col, visited, grid)
                    islands+=1
        return islands
    
    def bfs(self, row, col, visited, grid):
        n = len(grid)
        m = len(grid[0])

        visited[row][col] = 1
        q = deque()
        q.append((row, col))
        directions = [(0,-1),(-1,0),(0,1),(1,0)]
        while q:
            row, col = q.popleft()
            
            for deltarow , deltacol in directions:
                neighbor_row = row + deltarow
                neighbor_col = col + deltacol
                if 0 <= neighbor_row < n and 0 <= neighbor_col < m and grid[neighbor_row][neighbor_col] == '1' and visited[neighbor_row][neighbor_col] == 0:
                    visited[neighbor_row][neighbor_col] = 1
                    q.append((neighbor_row,neighbor_col))
