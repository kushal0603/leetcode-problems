class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = p = 0
        while p < n:
            p = 2 ** i
            if p == n:
                return True
            i +=1  
        return False