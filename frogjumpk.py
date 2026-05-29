class Solution:
    def solve(self, index, heights, k, dp):
        if index==0:
            return 0
        if dp[index]!=-1:
            return dp[index]
        mmsteps = float('inf')

        for j in range(1, k+1):
            if index-j>=0:
                jump_cost = self.solve(index-j, heights, k, dp) + abs(heights[index] - heights[index-j])
                mmsteps = min(mmsteps, jump_cost)
        dp[index] = mmsteps
        return dp[index]

    def frogJump(self, heights, k):
        n = len(heights)
        dp = [-1]*(n+1)
        return self.solve(n-1, heights, k, dp)