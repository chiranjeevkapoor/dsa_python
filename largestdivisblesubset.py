class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()


        dp = [1 for _ in range(n)]
        has = [-1 for _ in range(n)]

        for i in range(0, n):
            for j in range(0, i):
                if nums[i]%nums[j] == 0 and dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1
                    has[i] = j
        
        max_length = max(dp)
        curr_index = dp.index(max_length)
        lis = []

        while curr_index !=-1:
            lis.append(nums[curr_index])
            curr_index = has[curr_index]
        return lis[::-1]

        