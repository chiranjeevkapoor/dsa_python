from collections import deque
class Solution:
    def topoSort(self, V, edges):
        # Code here
        adj = [[] for _ in range(V)]
        visited = [0]*V
        for u, v in edges:
            adj[u].append(v)
        ans = deque()
        for i in range(V):
            if visited[i]==0:
                self.dfs(i, adj, ans, visited)
        
        return list(ans)
    
    def dfs(self, node, adj, ans, visited):
        visited[node]=1
        
        for neighbor in adj[node]:
            if visited[neighbor]==0:
                self.dfs(neighbor, adj, ans, visited)
        
        ans.appendleft(node)