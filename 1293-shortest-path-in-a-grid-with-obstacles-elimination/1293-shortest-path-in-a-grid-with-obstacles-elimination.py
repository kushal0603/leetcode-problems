class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n ==1: return 0
        queue = [(0,0,0)]
        step = 1
        visited = {(0,0):0}
        while queue:
            length = len(queue)
            new_queue = []
            for y,x,count in queue:
                for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                    tmp = count
                    if 0<=x+dx<n and 0<=y+dy<m and ((y+dy,x+dx) not in visited or visited[(y+dy,x+dx)] > tmp):
                        if grid[y+dy][x+dx] == 1: tmp += 1
                        if tmp > k: continue
                        if ((y+dy,x+dx,tmp)) not in new_queue: new_queue.append((y+dy,x+dx,tmp))
                        if (y+dy,x+dx) not in visited: visited[(y+dy,x+dx)] = 0
                        visited[(y+dy,x+dx)] = tmp
                        if (y+dy) == (m-1) and (x+dx) == (n-1): return step
            queue = new_queue
            step += 1
        return -1