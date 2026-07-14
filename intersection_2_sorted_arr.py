class Solution:
    def intersection(self, arr1, arr2):
        #code here
        n = len(arr1)
        m = len(arr2)
        i = j = 0
        arr = []
        def add_unique(val):
            if not arr or arr[-1]!=val:
                arr.append(val)
        while i < n and j < m:
            if arr1[i]==arr2[j]:
                add_unique(arr1[i])
                i+=1
                j+=1
            elif arr1[i]<arr2[j]:
                i+=1
            elif arr1[i]>arr2[j]:
                j+=1
        
        return arr