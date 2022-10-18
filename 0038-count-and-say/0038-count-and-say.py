class Solution:
    def countAndSay(self, n: int) -> str:
        ans=''
        if(n==1): # base case
            return '1' 
        co=self.countAndSay(n-1) # recursive call to store the result from predecessor of N
        if(len(co)==1): # if just a single digit is returned, the answer is" 1 +( concat ) digit" 
            return '1'+co
        lsf=0 #lsf = length of consecutive characters so far
        for i in range(len(co)):
            if(i==len(co)-1):
                ans+=str(lsf+1)+str(co[i])
            elif(co[i]!=co[i+1]): # if the next character is not the same, take the total cout of the character so far and add it to the final string
                ans+=str(lsf+1)+str(co[i])
                lsf=0
            else:
                lsf+=1
        return ans