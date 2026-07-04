from collections import deque
class Solution:
    def isCyclic(self, V, edges):
        # code here
        q = deque()
        adj = [[] for i in range(V)]
        indegree = [0]*V
        for u, v in edges:
            adj[u].append(v)
        
        for i in range(V):
            for el in adj[i]:
                indegree[el]+=1
        
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        count = 0
        
        while q:
            node = q.popleft()
            count+=1
            
            for el in adj[node]:
                indegree[el]-=1
                if indegree[el]==0:
                    q.append(el)
        
        if count==V:
            return False
        return True
                
        