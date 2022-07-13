class Solution:
    def climbStairs(self, n: int) -> int:
        
        total = sum ((math.factorial(n-i)/(math.factorial(n-2*i)*math.factorial(i))) for i in range(n//2+1))
        
        return int(total)