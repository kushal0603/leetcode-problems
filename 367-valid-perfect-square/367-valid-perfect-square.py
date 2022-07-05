class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        beg=1
        end=num
        m=(end+beg)//2
        while beg!=m:
            if m*m==num:
                return True
            if m*m>num:
                end=m    
            else:
                beg=m
                
            m=(end+beg)//2
        return False