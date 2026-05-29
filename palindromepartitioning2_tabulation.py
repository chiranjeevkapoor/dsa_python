def isPalindrome(i, j, s):
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True


def palindromePartitioning(s: str) -> int:
    n = len(s)
    dp = [0 for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        minCost = float('inf')
        for j in range(i, n):
            if isPalindrome(i, j, s):
                cost = 1 + dp[j+1]
                minCost = min(cost, minCost)
        dp[i] = minCost
    
    return dp[0]-1
            
