class Solution:
    def orangesRotting(self, G: List[List[int]]) -> int:
    	M, N, S, E, c = len(G), len(G[0]), [], sum(G,[]).count(1), 0
    	R = [(i,j) for i,j in itertools.product(range(M),range(N)) if G[i][j] == 2]
    	while E != 0:
    		for [i,j] in R:
    			for a,b in (i-1,j),(i,j+1),(i+1,j),(i,j-1):
    				if 0 <= a < M and 0 <= b < N and G[a][b] == 1: G[a][b], E, _ = 2, E - 1, S.append([a,b])
    		if len(S) == 0: return -1
    		R, S, c = S, [], c + 1
    	return c