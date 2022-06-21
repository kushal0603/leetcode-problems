class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        l=[1,1]
        l2=[]
        l3=[]
        l3.append([1])
        l3.append(l)
        for i in range(2,numRows):
            l2=[]
            l2.append(1)
            for j in range(len(l)-1):
                l2.append(l[j]+l[j+1])
            l2.append(1)
            l=l2.copy()
            l3.append(l2)
        return l3
