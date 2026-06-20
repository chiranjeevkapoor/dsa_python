from collections import deque


class Solution:
    def bfs(self, adj):
        ##we use a queue to keep track of current element that we are looking at

        visited = [0]*len(adj)
        visited[0] = 1
        q = deque()
        q.append(0)
        bfs = []
        while q:
            node = q.popleft()
            bfs.append(node)
            for el in adj[node]:
                if visited[el] == 0:
                    visited[el] = 1
                    q.append(el)
        return bfs
