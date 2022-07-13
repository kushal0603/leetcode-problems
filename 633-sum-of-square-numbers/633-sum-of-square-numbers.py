class Solution:
    
    import math
    
    def judgeSquareSum(self, c: int) -> bool:
        
        boundary = math.floor(math.sqrt(c))
        
        if boundary ** 2 == c: return True
        
        while boundary >= math.sqrt(c / 2):
            if math.sqrt(c - boundary ** 2) == math.floor(math.sqrt(c - boundary ** 2)): return True
            boundary -= 1
        
        return False