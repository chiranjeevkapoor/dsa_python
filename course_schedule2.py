from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u]+=1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)

            for neighbor in adj[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)
        
        if len(ans)!=numCourses:
            return []
        return ans



        

        