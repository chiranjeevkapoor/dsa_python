from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1]*n

        for i in range(n):
            if colors[i]==-1:
                if self.dfs(i, 0, graph, colors)==False:
                    return False
        
        return True
    
    def dfs(self, curr, color, graph, colors):
        colors[curr]=color

        for neighbor in graph[curr]:
            if colors[neighbor]==-1:
                if self.dfs(neighbor, 1-colors[curr], graph, colors)==False:
                    return False
            elif colors[neighbor]==colors[curr]:
                return False
        return True



        