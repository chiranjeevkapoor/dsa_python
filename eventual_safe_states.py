from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse = [[] for _ in range(n)]
        indegree = [0]*n
        for u in range(n):
            for v in graph[u]:
                reverse[v].append(u)
                indegree[u]+=1
        
        q = deque(i for i in range(n) if indegree[i]==0)

        safe = [False]*n

        while q:
            node = q.popleft()
            safe[node]=True

            for neighbor in reverse[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)
        
        return [i for i in range(n) if safe[i]]

        