class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win=[]
        lose=[]
        for i in matches:
            win.append(i[0])
            lose.append(i[1])
        l=[] #0 lose
        m=[] #1 lose
        c=Counter(lose)
        for i in range(len(win)):
            if c[win[i]]==0:
                l.append(win[i])
            if c[win[i]]==1:
                m.append(win[i])
            if c[lose[i]]==1:
                m.append(lose[i])
        
        l=list(set(l))
        m=list(set(m))
        l.sort()
        m.sort()

        return [l,m]
