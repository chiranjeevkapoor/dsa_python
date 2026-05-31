class Solution:
    def isSubsetSum (self, arr, sum):
        n = len(arr)
        dp = [[-1 for _ in range(sum+1)] for _ in range(n)]
        return self.solve(n-1, sum, arr, dp)
    
    def solve(self, index, target, arr, dp):
        if target<0:
            return False
        if dp[index][target] != -1:
            return dp[index][target]==1
        if index==0:
            return target==arr[index]
        if target == 0:
            return True
        
        pick = self.solve(index-1, target - arr[index], arr, dp)

        
        not_pick = self.solve(index-1, target, arr, dp)
        
        result = pick or not_pick
        dp[index][target] = 1 if result else 0
        
        return result