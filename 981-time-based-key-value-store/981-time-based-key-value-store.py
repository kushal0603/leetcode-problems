from heapq import *
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = collections.defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # -1 to make it a maxheap
        heappush(self.times[key], (timestamp*-1, value))
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        for value in self.times[key]:
            if abs(value[0]) <= timestamp:
                res = value[1]
                break
        return res