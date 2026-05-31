class Solution:
    def isSubsetSum (self, arr, sum):
        n = len(arr)
        dp = [[0 for _ in range(sum+1)] for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = True
        
        if arr[0]<=sum:
            dp[0][arr[0]] = True
        
        for index in range(1, n):
            for target in range(sum+1):
                not_take = dp[index-1][target]
                take = False
                if target>=arr[index]:
                    take = dp[index-1][target-arr[index]]
                dp[index][target] = take or not_take
        
        return dp[n-1][sum]