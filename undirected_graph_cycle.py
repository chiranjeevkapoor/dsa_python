from collections import deque
class Solution:
	def isCycle(self, V, edges):
		adj = [[] for _ in range(V)]
		
		for u, v in edges:
		    adj[u].append(v)
		    adj[v].append(u)
		
		self.visited = [0]*V
		
		for i in range(V):
		    if self.visited[i]==0:
		        if self.detect(adj, i):
		            return True
		
		return False
	
	def detect(self, adj, src):
	    q = deque()
	    q.append((src, -1))
	    self.visited[src] = 1
	    while q:
	        node, parent = q.popleft()
	        for neighbor in adj[node]:
	            if not self.visited[neighbor]:
	                q.append((neighbor, node))
	                self.visited[neighbor] = 1
	            elif neighbor != parent:
	                return True
	    return False
		        