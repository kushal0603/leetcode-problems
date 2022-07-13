class Solution:
    def searchRange(self, n: List[int], t: int) -> List[int]:
    	return (lambda x,y: [-1,-1] if x == y else [x,y-1])(bisect.bisect_left(n,t),bisect.bisect(n,t))