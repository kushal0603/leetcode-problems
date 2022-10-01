class DSU:
    def __init__(self):
        self.parent = [i for i in range(26)]
        
    def find(self, n):
        x = n
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        self.parent[self.find(u)] = self.find(v)
        
class Solution:
    def __init__(self):
        self.m = defaultdict(int)
        for i in range(ord("a"), ord("z")):
            self.m[chr(i)] = i - ord("a")
    
    def equationsPossible(self, equations: List[str]) -> bool:
        equal = DSU()
        
        for i in equations:
            if i[1] == "=":
                equal.union(self.m[i[0]],self.m[i[-1]])
        for i in equations:
            
            if i[1] == '!' and equal.find(self.m[i[0]]) == equal.find(self.m[i[-1]]):
                    return False
        return True
                