class Solution:
    def firstUniqChar(self, s):
        dict1 = Counter(s)
    
        for i in s:
            if dict1[i] == 1:
                return s.index(i)
        
        return -1