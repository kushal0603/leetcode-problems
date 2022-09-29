class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
		# 1. Create 2 pointers at the start and the end index positions
        startPointer = 0
        endPointer = len(arr) - 1
		# 2. Loop and move pointer following the condition 
		#    until the distance between start and end pointer < k
        while endPointer - startPointer >= k:
            if abs(arr[startPointer] - x) <= abs(arr[endPointer] - x):
                endPointer -= 1
            else:
                startPointer += 1
		# 3. Create subarray following two pointers and return
        return arr[startPointer: endPointer + 1]