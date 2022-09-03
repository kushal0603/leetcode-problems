class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        def bt(cur: int, i: int = 1):
            if i == n:
                yield cur
            else:
                u = cur % 10
                cur *= 10
                if u + k <= 9:
                    yield from bt(cur + u + k, i + 1)
                if k > 0 and u - k >= 0:
                    yield from bt(cur + u - k, i + 1)
                   
        def main():
            for m in range(1, 10):
                yield from bt(m)
                
        return list(main())
    #backtracing