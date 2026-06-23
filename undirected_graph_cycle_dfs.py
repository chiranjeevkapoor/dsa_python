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
		        if self.dfs(adj, i, -1):
		            return True
		
		return False
		
	def dfs(self, adj, src, parent):
	    self.visited[src] = 1
	    
	    for neighbor in adj[src]:
	        if not self.visited[neighbor]:
	            if self.dfs(adj, neighbor, src):
	                return True
	        elif neighbor != parent:
	            return True
	    return False