class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        for i in s:
            # print(ans)
            if i==']':
                pos = len(ans)-1
                temp = ""
                while ans[pos]!='[':
                    temp = ans[pos] +temp
                    pos-=1
                # print("temp: ",temp)
                num = 0
                pos-=1
                c = 1
                while pos>=0 and ans[pos] in "0123456789":
                    num+= c*(ord(ans[pos])-ord("0"))
                    pos-=1
                    c*=10
                # print("num: ",num)
                ans = ans[:pos+1]+temp*num
            else:
                ans+=i
        return ans