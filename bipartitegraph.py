from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1]*n

        for i in range(n):
            if colors[i]==-1:
                q = deque([i])
                colors[i]=0

                while q:
                    curr = q.popleft()

                    for neighbor in graph[curr]:
                        if colors[neighbor] == -1:
                            colors[neighbor]=1-colors[curr]
                            q.append(neighbor)
                        elif colors[neighbor]==colors[curr]:
                            return False
        return True


        