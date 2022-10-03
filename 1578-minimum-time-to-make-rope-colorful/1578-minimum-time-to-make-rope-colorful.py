class Solution:
    # simple Heap implementation in python
    def minCost(self, colors: str, nt: List[int]) -> int:
        i, res = 1, 0
        while i < len(colors):
            heap = []
            while i < len(colors) and colors[i] == colors[i - 1]:
                heappush(heap, nt[i - 1]) # Keep adding to heap if same
                i += 1
            if heap: heappush(heap, nt[i - 1]) # add the last one as it was left
            while len(heap) > 1:
                res += heappop(heap) # keep popping and adding to the result time lowest time needed first
            heap.clear() # clear the heap for future use
            i += 1 # since colors[i] != colors[i - 1] if we came till here so simply increase i
        return res