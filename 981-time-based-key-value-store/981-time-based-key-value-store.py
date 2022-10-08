class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        array = self.map[key]
        low, high = 0, len(array) - 1
        while low <= high:
            mid = low + math.floor((high - low) / 2)
            t, v = array[mid]
            if t == timestamp:
                return v
            elif t < timestamp:
                low = mid + 1
            else:
                high = mid - 1
        
        value = str()
        if low > 0:
            _, v = array[low - 1]
            value += v
        
        return value