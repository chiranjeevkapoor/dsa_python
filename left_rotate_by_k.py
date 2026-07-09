def rotateArray(arr: list, k: int) -> list:
    n = len(arr)
    temp = arr[:k]

    for i in range(k, n):
        arr[i-k] = arr[i]
    
    for i in range(n-k, n):
        arr[i] = temp[i - (n-k)]
    return arr



class Solution:
    def rotateArr(self, arr, d):
        #code here
        n = len(arr)
        d = d%n
        
        def reverse(l, r):
            while l<r:
                arr[l], arr[r] = arr[r], arr[l]
                l+=1
                r-=1
        
        reverse(0, d-1)
        reverse(d, n-1)
        reverse(0, n-1)
        