class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        
        def dfs(src):
            seen.add(src)
            
            for i in rooms[src]:
                if i not in seen:
                    dfs(i)
        dfs(0)
        return len(rooms) == len(seen)