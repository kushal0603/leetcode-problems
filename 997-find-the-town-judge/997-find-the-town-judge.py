class Solution:
	def findJudge(self, n: int, trust: List[List[int]]) -> int:
		indegree=[0]*n
		graph=defaultdict(list)
		for edge in trust:
			indegree[edge[1]-1]+=1
			graph[edge[0]].append(edge[1])

		for i in range(len(indegree)):
			if indegree[i]==n-1 and not graph[i+1]:
				return i+1
		return -1