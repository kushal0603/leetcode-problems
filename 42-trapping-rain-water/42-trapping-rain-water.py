class Solution:
    def trap(self, s: List[int]) -> int:
        left,right = [s[0]]+[0]*(len(s)-1), [0]*(len(s)-1) + [s[-1]]
        for i in range(1,len(s)):
            left[i]=max(left[i-1],s[i])
            right[-i]=max(right[-i+1],s[-i])
        return sum([max(min(left[i-1],right[i+1])-s[i],0) for i in range(1,len(s)-1)])