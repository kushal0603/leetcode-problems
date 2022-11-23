SQUARES = set(i*i for i in range(100, 0, -1))
IS_PS = [(i in SQUARES) for i in range(10001)]
class Solution:
    @lru_cache(None)
    def numSquares(self, n: int) -> int:
        if IS_PS[n]: return 1
        return 1 + min(self.numSquares(n-s) for s in SQUARES if s < n)