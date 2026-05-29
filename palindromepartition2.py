def isPalindrome(i, j, s):
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True
def solve(i, s, dp):
    n = len(s)
    if i==n:
        return 0
    if dp[i] != -1:
        return dp[i]
    minCost = float('inf')

    for j in range(i, n):
        if isPalindrome(i, j, s):
            cost = 1 + solve(j+1, s, dp)
            minCost = min(cost, minCost)
    dp[i] = minCost
    return minCost

def palindromePartitioning(string: str) -> int:
    n = len(string)
    dp = [-1 for _ in range(n)]
    return solve(0, string, dp)-1
