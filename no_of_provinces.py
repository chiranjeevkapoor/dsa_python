class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = [0]*len(isConnected[0])
        self.dfs_res = []
        self.provinces = 0

        for i in range(0, len(isConnected[0])):
            if self.visited[i] == 0:
                self.perform_dfs(i, isConnected)
                self.provinces+=1
        return self.provinces

    def perform_dfs(self, node, isConnected):
        self.visited[node] = 1
        self.dfs_res.append(node)
        for el in range(0, len(isConnected[node])):
            if self.visited[el] == 0 and isConnected[node][el] == 1:
                self.perform_dfs(el, isConnected)
        