class Solution:
    def isCyclic(self, V, edges):
        # code here
        visited = [0]*V
        pathVisited = [0]*V
        adj = [[] for _ in range(V)]
        
        for u, v in edges:
            adj[u].append(v)
            
        for i in range(V):
            if self.dfs(i, visited, pathVisited, adj)==True:
                return True
        
        return False
    
    
    def dfs(self, el, visited, pathVisited, adj):
        visited[el]=1
        pathVisited[el] = 1
        
        for neighbor in adj[el]:
            if visited[neighbor]==0:
                if self.dfs(neighbor, visited, pathVisited, adj)==True:
                    return True
            elif visited[neighbor]==1 and pathVisited[neighbor]==1:
                return True
        pathVisited[el]=0
        return False
            
        
        
        
        