class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        l1=[]
        sum=0
        
        for i in nums:
            if i%2==0:
                sum=sum+i
                
        for j in queries:
            if nums[j[1]]%2==0:
                sum=sum-nums[j[1]]
                
            nums[j[1]]=nums[j[1]]+j[0]
            
            if nums[j[1]]%2==0:
                sum=sum+nums[j[1]]  
                
            l1.append(sum)
            
        return l1