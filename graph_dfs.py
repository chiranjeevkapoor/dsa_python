
class Solution:
    def dfs(self, adj):
        self.visited = [0]*len(adj)
        self.dfs_result = []
        self.perform_dfs(0, adj)
        return self.dfs_result

    def perform_dfs(self, node, adj):
        self.visited[node] = 1
        self.dfs_result.append(node)
        for el in adj[node]:
            if self.visited[el] == 0:
                self.perform_dfs(el, adj)