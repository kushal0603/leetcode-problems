class Solution:
    def reverseWords(self, s: str) -> str:
        string=list(s.split(" "))
        string.reverse()
        l=len(string)
        i=0
        #removing additional spaces
        while i<l:
            if string[i]=="":
                string.pop(i)
                l-=1
            else:
                i+=1
        return " ".join(string)