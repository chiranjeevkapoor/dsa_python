class Solution:
    def checkPossible(self, str1, str2):
        if len(str1) != len(str2)+1:
            return False
        first = 0
        second = 0
        while first<len(str1):
            if second<len(str2) and str1[first]==str2[second]:
                first+=1
                second+=1
            else:
                first+=1
        if first == len(str1) and second == len(str2):
            return True
        else:
            return False 

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        n = len(words)
        dp = [1 for _ in range(n)]
        maxiLength = 1
        for i in range(n):
            for j in range(i):
                if self.checkPossible(words[i], words[j]) and dp[i]<dp[j]+1:
                    dp[i] = dp[j] + 1
                maxiLength = max(maxiLength, dp[i])
        
        return maxiLength