class Solution:
    def findUnion(self, a, b):
        i = j = 0
        arr = []
        
        def add_unique(val):
            if not arr or arr[-1]!=val:
                arr.append(val)
        while i < len(a) and j < len(b):
            if a[i]==b[j]:
                add_unique(a[i])
                i+=1
                j+=1
            elif a[i]<b[j]:
                add_unique(a[i])
                i+=1
            elif a[i]>b[j]:
                add_unique(b[j])
                j+=1
        
        while i<len(a):
            add_unique(a[i])
            i+=1
        while j<len(b):
            add_unique(b[j])
            j+=1
            
        return arr
            