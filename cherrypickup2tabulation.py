class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[[0 for _ in range(m)] for _ in range(m)] for _ in range(n)]
        

        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    dp[n-1][j1][j2] = grid[n-1][j1]
                else:
                    dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2]
        

        for i in range(n-2, -1, -1):
            for j1 in range(m):
                for j2 in range(m):
                    maxi = float('-inf')
                    for dj1 in range(-1, 2):
                        for dj2 in range(-1, 2):
                            value = 0
                            if j1 == j2:
                                value = grid[i][j1]
                            else:
                                value = grid[i][j1] + grid[i][j2]
                            if j1+dj1>=0 and j1+dj1<m and j2+dj2>=0 and j2+dj2<m:
                                value += dp[i+1][j1+dj1][j2+dj2]
                            else:
                                value += float('-inf')
                            maxi = max(maxi, value) 
                    dp[i][j1][j2] = maxi
        
        return dp[0][0][m-1]
        
