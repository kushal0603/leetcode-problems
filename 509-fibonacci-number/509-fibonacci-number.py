class Solution:
    def fib(self, N):
		dp = []
		dp.append(0)
		dp.append(1)
		if N==0 :
			return 0;

		for i in range(2,N +1) :
			dp.append(dp[-1] + dp[-2])

		return dp[-1]