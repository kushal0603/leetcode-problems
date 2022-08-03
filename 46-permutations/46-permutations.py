class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output=[]
        def recursion(array,path=[]):
            if len(array)==0:
                return [path]
            for i in array:
                new=array.copy()
                new.remove(i)
                cc=recursion(new,path+[i])
                if cc!=None:
                    for i in cc:
                        output.append(i)
                    
        
        recursion(nums)
        return output