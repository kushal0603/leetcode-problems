class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo={(m-1,n-1): 1};
        def go(x=0,y=0):
            if x == m or y == n: return 0;
            elif (x,y) in memo: return memo[(x,y)];
            memo[(x,y)] = go(x+1,y) + go(x,y+1);
            return memo[(x,y)];
        return go();