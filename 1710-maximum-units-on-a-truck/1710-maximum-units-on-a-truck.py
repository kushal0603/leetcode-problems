class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        units, i = 0, 0
        while truckSize > 0 and i < len(boxTypes):
            units += min(truckSize,boxTypes[i][0]) * boxTypes[i][1]
            truckSize -= boxTypes[i][0]
            i += 1
        return units