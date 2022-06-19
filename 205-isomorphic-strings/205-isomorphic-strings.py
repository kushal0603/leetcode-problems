class Solution:
     def isIsomorphic(self, s: str, t: str) -> bool:
        ma, mb = {}, {}
        
        for a, b in zip(s, t):
            if (a in ma and ma[a] != b) or (b in mb and mb[b] != a): return False
            ma[a], mb[b] = b, a
                
        return True
        