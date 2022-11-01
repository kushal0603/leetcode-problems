
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        times = [(plantTime[i], growTime[i]) for i in range(len(plantTime))]
        times = sorted(times, key=lambda x: x[1], reverse=True)

        time = 0
        mx = 0
        for plantTime, growTime in times:
            time += plantTime
            mx = max(mx, time + growTime)
        
        return mx