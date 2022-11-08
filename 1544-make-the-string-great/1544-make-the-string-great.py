class Solution:
    def makeGood(self, s: str) -> str:
        l=[]
        # l.append(s[0])
        for i in range(0,len(s)):
            if len(l)==0:
                l.append(s[i])
            else:
                if ord(s[i])-ord(l[-1])==32 or ord(l[-1])-ord(s[i])==32:
                    l.pop()
                else:
                    l.append(s[i])
        return "".join(l)