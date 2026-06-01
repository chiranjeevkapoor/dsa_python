class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = 0
        for i in range(n):
            s+=nums[i]
        
        if s%2!=0:
            return False
        s=s//2
        dp = [[False for _ in range(s+1)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = True
        
        if nums[0]<=s:
            dp[0][nums[0]] = True
        
        for index in range(1, n):
            for target in range(s+1):
                not_take = dp[index-1][target]
                take = False
                if nums[index] <= target:
                    take = dp[index-1][target-nums[index]]
                result = take or not_take
                dp[index][target] = result
        
        return dp[n-1][s]

        
