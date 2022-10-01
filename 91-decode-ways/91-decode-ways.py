class Solution:
    def numDecodings(self, s: str) -> int:
        p2 = 0
        p1 = 1
        curr = 0

        #Bottom up solution
        for i in range(len(s) -1, -1, -1):
            curr = 0
            #If s[i] is 0 we can't do anything to it hence we set it as 0.
            if s[i] == "0":
                curr = 0
            elif s[i] == "2":
                #Check if 2 can be a combination with s[i + 1], if so we add the two
                if i + 1 < len(s) and s[i + 1] in "0123456":
                    curr = p1 + p2
                else:
                    curr = p1
            elif s[i] == "1":
                #If 1 we can add the previous 2 combinations as what follows 1 can be anything.
                curr = p1 + p2
            else:
                #If val != 1 or 2 it can not combine, hence it has only 1 form. We do not add
                curr = p1
            
            #Updating previous combination by moving output[i + 1] -> output[i + 2] 
            #and curr -> output[i + 1]
            p2 = p1
            p1 = curr
        
        return curr