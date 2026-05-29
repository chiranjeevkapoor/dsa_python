#User function Template for python3
class Solution:
    def maximumPath(self, mat):
        n = len(mat)
        m = len(mat[0])
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        maxi = float('-inf')
        for j in range(m):
            maxi = max(maxi, self.solve(n-1, j, mat, dp))

        return maxi
    
    def solve(self, i, j, matrix, dp):
        n = len(matrix)
        m = len(matrix[0])
        if j < 0 or j > m-1:
            return float('-inf')
        if dp[i][j] != -1:
            return dp[i][j]
        if i == 0 :
            return matrix[i][j]
        
        up = self.solve(i-1, j, matrix, dp)
        upleft = self.solve(i-1, j-1, matrix, dp)
        upright = self.solve(i-1, j+1, matrix, dp)
        
        maxi = max(up, upleft, upright) + matrix[i][j]
        dp[i][j] = maxi
        return maxi