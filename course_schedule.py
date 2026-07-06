from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        visited_count=0
        indegree=[0]*numCourses
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course]+=1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            current = q.popleft()
            visited_count+=1

            for neighbor in adj[current]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)

        
        return numCourses==visited_count


        