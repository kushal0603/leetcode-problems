class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        if k > n:
            return False
    
        s1Count = collections.Counter(s1)
        s2Count = collections.Counter(s2[i] for i in range(k))
        if s1Count == s2Count:
            return True
        
        for i in range(k, n):
            s2Count[s2[i-k]] -= 1
            s2Count[s2[i]] += 1
            if s1Count == s2Count:
                return True
        
        return False