import heapq
class Solution:
    def spanningTree(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        visited = [0]*V
        pq = []
        ##(wt, node)
        heapq.heappush(pq, (0, 0))
        sumwts = 0
        while pq:
            wt, node = heapq.heappop(pq)
            if visited[node] == 1:
                continue
            visited[node] = 1
            sumwts += wt
            for neighbor, w in adj[node]:
                if visited[neighbor] == 0:
                    heapq.heappush(pq, (w, neighbor))
        
        return sumwts