#User function Template for python3
class DisjointSet:
    def __init__(self, n):
        self.size = [1]*(n+1)
        self.parent = list(range(n+1))

    def find_upar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_upar(self.parent[node])
        return self.parent[node]
    
    def union_by_size(self, u, v):
        ulp_u = self.find_upar(u)
        ulp_v = self.find_upar(v)

        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
class Solution:
    def numProvinces(self, adj, V):
        ds = DisjointSet(V)
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1:
                    ds.union_by_size(i, j)
        
        count = 0
        
        for i in range(V):
            if ds.parent[i] == i:
                count+=1
        
        return count