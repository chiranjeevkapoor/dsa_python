from collections import deque
class Solution:
    def topoSort(self, V, edges):
        # Code here
        q = deque()
        adj = [[] for i in range(V)]
        visited = [0]*V
        indegree = [0]*V
        for u, v in edges:
            adj[u].append(v)
        
        for i in range(V):
            for el in adj[i]:
                indegree[el]+=1
        
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        ans = []
        
        while q:
            node = q.popleft()
            ans.append(node)
            
            for el in adj[node]:
                indegree[el]-=1
                if indegree[el]==0:
                    q.append(el)
        
        return ans
            