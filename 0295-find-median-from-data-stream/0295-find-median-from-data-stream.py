from sortedcontainers import SortedList
class MedianFinder:

	def __init__(self):
		self.res=SortedList([])

	def addNum(self, num: int) -> None:
		self.res.add(num)

	def findMedian(self) -> float:
		n = len(self.res)
		if(n % 2 == 0):
			return(self.res[n//2] + self.res[n//2-1])/2
		else:
			return(self.res[n//2])