class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        self.visited = [0]*n
        self.complete_components = 0

        for el in range(n):
            if self.visited[el] == 0:
                components = []
                self.dfs(el, adj, components)
                
                v = len(components)
                edges = sum(len(adj[node]) for node in components)

                if edges == v*(v-1):
                    self.complete_components+=1
        
        return self.complete_components
    
    def dfs(self, node, adj, components):
        self.visited[node] = 1
        components.append(node)
        for el in adj[node]:
            if self.visited[el] == 0:
                self.dfs(el, adj, components)
        