class Solution:
    def countDistinctIslands(self, grid):
        # code here
        n = len(grid)
        m = len(grid[0])
        st = set()
        visited = [[0 for _ in range(m)] for _ in range(n)]
        
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='L' and visited[i][j]==0:
                    vec = []
                    self.dfs(i, j, grid, visited, i, j, vec)
                    st.add(tuple(vec))
        
        return len(st)
        
    def dfs(self, row, col, grid, visited, baseRow, baseCol, vec):
        n = len(grid)
        m = len(grid[0])
        visited[row][col]=1
        vec.append((row-baseRow, col-baseCol))
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        
        for drow, dcol in directions:
            nrow = row + drow
            ncol = col + dcol
            if 0<=nrow<n and 0<=ncol<m and grid[nrow][ncol]=="L" and visited[nrow][ncol]==0:
                self.dfs(nrow, ncol, grid, visited, baseRow, baseCol, vec)
                