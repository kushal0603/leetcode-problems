class Engineer:
    def __init__(self, speed, efficiency):
        self.s = speed
        self.e = efficiency
    
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        eng, mod, res = [], 10**9 + 7, 0
        
        for i in range(n):
            eng.append(Engineer(speed[i], efficiency[i]))
        
        eng = sorted(eng, key=lambda x: x.e, reverse=True)
        
        heap, sum_speed = [], 0
        for i in range(n):
            heappush(heap, eng[i].s)
            sum_speed += eng[i].s
            
            if len(heap) > k:
                sum_speed -= heappop(heap)
            
            res = max(res, eng[i].e * sum_speed)
        
        return res % mod
