class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        S = sum(matchsticks)
        
        if S % 4 != 0: return False
        target = S // 4
        
        total = (1<<n)-1
        
        @cache
        def check(mask, s):
            if mask == total: return s == 0
            for i in range(n):
                if mask & (1<<i): continue
                L = s+matchsticks[i]
                if L == target and check(mask | (1<<i), 0):
                    return True
                if L < target and check(mask | (1<<i), L):
                    return True
            return False
        
        return check(0, 0)