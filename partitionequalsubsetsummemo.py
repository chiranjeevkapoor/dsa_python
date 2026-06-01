class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        s = 0

        for i in range(n):
            s+=nums[i]
        
        if s%2!=0:
            return False
        s=s//2
        dp = [[-1 for _ in range(s+1)] for _ in range(n)]
        return self.solve(n-1, nums, s, dp)
    
    def solve(self, index, nums, target, dp):
        if target<0:
            return False
        if index==0:
            return target==nums[index]
        if target==0:
            return True
        if dp[index][target] != -1:
            return dp[index][target]
        
        pick = self.solve(index-1, nums, target-nums[index], dp)
        not_pick = self.solve(index-1, nums, target, dp)
        
        result = pick or not_pick
        dp[index][target] = result
        return result
        
