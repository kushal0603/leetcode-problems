from collections import Counter
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        #get counts of each number in the input list
        counts = Counter(nums)
        tails = Counter()
        for i in nums:
            if counts[i] == 0:
                continue # if counts[i] == 0, we've used up all instances of that number
            elif tails[i] > 0:
                tails[i] -=1
                tails[i+1]+=1
            elif (counts[i+1]>0 and counts[i+2]>0):
                counts[i+1]-=1
                counts[i+2]-=1
                tails[i+3]+=1
            
            else:
                return False
        
            counts[i]-=1
        
        return True