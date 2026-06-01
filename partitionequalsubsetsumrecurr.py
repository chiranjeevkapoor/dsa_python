class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = 0

        for i in range(n):
            s+=nums[i]
        
        if s%2==1:
            return False

        return self.solve(n-1, nums, s/2)
    
    def solve(self, index, nums, target):
        if index==0:
            return target==nums[index]
        if target==0:
            return True
        
        if self.solve(index-1, nums, target-nums[index]):
            return True
        if self.solve(index-1, nums, target):
            return True
        
        return False
        
