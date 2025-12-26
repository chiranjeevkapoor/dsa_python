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
        if ulp_u == ulp_v:
            return

        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]



if __name__ == '__main__':
    ds = DisjointSet(7)
    ds.union_by_size(1, 2)
    ds.union_by_size(2, 3)
    ds.union_by_size(4, 5)
    ds.union_by_size(6, 7)
    ds.union_by_size(5, 6)

    # Check if 3 and 7 are in the same set
    if ds.find_upar(3) == ds.find_upar(7):
        print("Same")
    else:
        print("Not same")

    ds.union_by_size(3, 7)

    # Check again after union
    if ds.find_upar(3) == ds.find_upar(7):
        print("Same")
    else:
        print("Not same")