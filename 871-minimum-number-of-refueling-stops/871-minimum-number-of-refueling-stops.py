class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        count = 0
        heap = []
        heapify(heap)
        l,r = 0,bisect_right(stations,startFuel,key=lambda i:i[0])
        if(startFuel>=target):
            return 0
        if(r==0): return -1
        while(startFuel<target):
            count+=1
            for i in range(l,r): heappush(heap,-1*stations[i][1])
            if(len(heap)==0 and startFuel<target): return -1
            l = r
            startFuel+=(heappop(heap)*-1)
            r = bisect_right(stations,startFuel,key=lambda i:i[0])
        if(startFuel<target): return -1
        return count
        