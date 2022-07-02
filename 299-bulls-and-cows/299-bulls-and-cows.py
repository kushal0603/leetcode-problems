class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        m = {}
        a, b = 0, 0
        s = set()
        
        for i, c in enumerate(secret):
            if c not in m: m[c] = set()
            m[c].add(i)
        
        for i, c in enumerate(guess):
            if c in m and i in m[c]: 
                a += 1
                m[c].remove(i)
                s.add(i)
                
            if c in m and not m[c]: m.pop(c)
        
        for i, c in enumerate(guess):
            if i in s: continue
            
            if c in m:
                b += 1
                m[c].pop()
                
            if c in m and not m[c]: m.pop(c)
                
        return str(a)+"A"+str(b)+"B"