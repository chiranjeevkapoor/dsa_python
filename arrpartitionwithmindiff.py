from typing import List

def minSubsetSumDifference(nums: List[str], n: int) -> int:
    n= len(nums)
    s = sum(nums)
    prev = [False]*(s+1)
    prev[0] = True
    if nums[0]<=s:
        prev[nums[0]] = True
    
    for index in range(1, n):
        curr = [False]*(s+1)
        curr[0] = True
        for target in range(1, s+1):
            not_take = prev[target]
            take = False
            if nums[index]<=target:
                take = prev[target-nums[index]]
            curr[target] = take or not_take
        prev = curr
    
    dp = prev

    totalsum = 0
    totalsum = sum(nums)
    mini = float('inf')

    for i in range(0, totalsum+1):
        if dp[i] == True:
            s1 = i
            s2 = totalsum - s1
            mini = min(mini, abs(s2-s1))
    return mini