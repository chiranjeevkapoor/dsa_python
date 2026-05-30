class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        return self.solve(0, 0, m-1, grid)
    
    def solve(self, i, j1, j2, grid):
        n = len(grid)
        m = len(grid[0])

        if j1<0 or j1>=m or j2<0 or j2>=m:
            return float('-inf')
        
        if i == n-1:
            if j1 == j2:
                return grid[i][j1]
            else:
                return grid[i][j1] + grid[i][j2]
        maxi = 0

        for dj1 in range(-1, 2):
            for dj2 in range(-1, 2):
                if j1 == j2:
                    maxi =  max(maxi, grid[i][j1] + self.solve(i+1, j1+dj1, j2+dj2, grid))
                else:
                    maxi = max(maxi, grid[i][j1] + grid[i][j2] + self.solve(i+1, j1+dj1, j2+dj2, grid))
        
        return maxi

        