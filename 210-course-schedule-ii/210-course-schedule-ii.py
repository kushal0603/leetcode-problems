class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = defaultdict(list)
        for x in prerequisites:
            preq[x[0]] += [x[1]]

        order = []
        visited = {}
        def isCycleDFS(node):
            if node in visited:
                return visited[node]
            visited[node] = True
            for n in preq[node]:
                if isCycleDFS(n): return True
            visited[node] = False
            order.append(node)
            return False
            
        for i in range(numCourses):
            if isCycleDFS(i): return []
            
        return order